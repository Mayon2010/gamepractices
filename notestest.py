import tkinter as tk
from tkinter import messagebox, filedialog
import os
import json

# Main Application
class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")
        self.root.geometry("600x500")
        
        # Set up folders
        self.notes_folder = "notes"
        if not os.path.exists(self.notes_folder):
            os.makedirs(self.notes_folder)
        
        self.current_folder = None
        self.current_note = None

        # Assets folder and icon loading (icons must be kept referenced on the instance)
        self.assets_folder = "notesassets"
        self.icons = {}
        for key in ("create", "open", "exit", "save_note", "save", "back", "folder", "note", "delete", "export"):
            path = os.path.join(self.assets_folder, f"{key}.png")
            try:
                self.icons[key] = tk.PhotoImage(file=path)
            except Exception:
                # If loading fails, set None — buttons will show text only
                self.icons[key] = None

        # Show home screen
        self.show_home_screen()
    
    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # HOME SCREEN
    def show_home_screen(self):
        """Display the home screen"""
        self.clear_window()
        
        title = tk.Label(self.root, text="Notes App", font=("Arial", 24, "bold"))
        title.pack(pady=20)
        
        # Create note button
        create_btn = tk.Button(
            self.root,
            text="Create New Note",
            image=self.icons.get('create'),
            compound='left',
            font=("Arial", 12),
            width=30,
            padx=8,
            pady=6,
            anchor='w',
            command=self.show_create_note_screen
        )
        create_btn.pack(pady=10)
        
        # Open notes button
        open_btn = tk.Button(
            self.root,
            text="Open Existing Notes",
            image=self.icons.get('open'),
            compound='left',
            font=("Arial", 12),
            width=30,
            padx=8,
            pady=6,
            anchor='w',
            command=self.show_folders_screen
        )
        open_btn.pack(pady=10)
        
        # Exit button
        exit_btn = tk.Button(
            self.root,
            text="Exit",
            image=self.icons.get('exit'),
            compound='left',
            font=("Arial", 12),
            width=30,
            padx=8,
            pady=6,
            anchor='w',
            command=self.root.quit
        )
        exit_btn.pack(pady=10)
    
    # CREATE NOTE SCREEN
    def show_create_note_screen(self):
        """Screen to create a new note"""
        self.clear_window()
        
        # Title
        title = tk.Label(self.root, text="Create New Note", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # Note name input
        name_label = tk.Label(self.root, text="Note Name:", font=("Arial", 10))
        name_label.pack()
        
        name_entry = tk.Entry(self.root, width=40, font=("Arial", 10))
        name_entry.pack(pady=5)
        
        # Folder selection
        folder_label = tk.Label(self.root, text="Folder:", font=("Arial", 10))
        folder_label.pack()
        
        # Get folders list
        folders = self.get_folders()
        
        folder_var = tk.StringVar(value="General")
        folder_dropdown = tk.OptionMenu(self.root, folder_var, *folders, "New Folder")
        folder_dropdown.pack(pady=5)
        
        # Text area for note
        text_label = tk.Label(self.root, text="Note Content:", font=("Arial", 10))
        text_label.pack()
        
        text_area = tk.Text(self.root, height=10, width=50, font=("Arial", 10))
        text_area.pack(pady=10)
        
        # Save button
        def save_note():
            name = name_entry.get()
            folder = folder_var.get()
            content = text_area.get("1.0", tk.END)
            
            if not name:
                messagebox.showerror("Error", "Please enter a note name")
                return
            
            if folder == "New Folder":
                new_folder = tk.simpledialog.askstring("New Folder", "Folder name:")
                if not new_folder:
                    return
                folder = new_folder
            
            # Create folder if needed
            folder_path = os.path.join(self.notes_folder, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Save note
            note_path = os.path.join(folder_path, f"{name}.txt")
            with open(note_path, "w") as f:
                f.write(content)
            
            messagebox.showinfo("Success", f"Note '{name}' saved in folder '{folder}'")
            self.show_home_screen()
        
        save_btn = tk.Button(
            self.root,
            text="Save Note",
            image=self.icons.get('save_note'),
            compound='left',
            font=("Arial", 10),
            command=save_note
        )
        save_btn.pack(pady=10)
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="Back",
            image=self.icons.get('back'),
            compound='left',
            font=("Arial", 10),
            command=self.show_home_screen
        )
        back_btn.pack(pady=5)
    
    # FOLDERS SCREEN
    def show_folders_screen(self):
        """Show list of folders to open"""
        self.clear_window()
        
        title = tk.Label(self.root, text="Select Folder", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        folders = self.get_folders()
        
        if not folders:
            no_label = tk.Label(self.root, text="No folders found", font=("Arial", 12))
            no_label.pack(pady=20)
        else:
            # Create buttons for each folder
            for folder in folders:
                btn = tk.Button(
                    self.root,
                    text=folder,
                    image=self.icons.get('folder'),
                    compound='left',
                    font=("Arial", 11),
                    padx=8,
                    pady=6,
                    anchor='w',
                    command=lambda f=folder: self.show_notes_in_folder(f)
                )
                # let the button expand horizontally so long folder names are visible
                btn.pack(pady=5, fill='x', padx=20)
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="Back",
            image=self.icons.get('back'),
            compound='left',
            font=("Arial", 10),
            command=self.show_home_screen
        )
        back_btn.pack(pady=10)
    
    # NOTES IN FOLDER SCREEN
    def show_notes_in_folder(self, folder_name):
        """Show all notes in a specific folder"""
        self.clear_window()
        self.current_folder = folder_name
        
        title = tk.Label(self.root, text=f"Folder: {folder_name}", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # Get notes in this folder
        folder_path = os.path.join(self.notes_folder, folder_name)
        notes = self.get_notes_in_folder(folder_path)
        
        if not notes:
            no_label = tk.Label(self.root, text="No notes in this folder", font=("Arial", 12))
            no_label.pack(pady=20)
        else:
            # Create buttons for each note
            for note in notes:
                note_name = note.replace(".txt", "")
                btn = tk.Button(
                    self.root,
                    text=note_name,
                    image=self.icons.get('note'),
                    compound='left',
                    font=("Arial", 11),
                    padx=8,
                    pady=6,
                    anchor='w',
                    command=lambda n=note_name: self.show_note_screen(folder_name, n)
                )
                # expand so long note names aren't cut off
                btn.pack(pady=5, fill='x', padx=20)
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="Back",
            image=self.icons.get('back'),
            compound='left',
            font=("Arial", 10),
            command=self.show_folders_screen
        )
        back_btn.pack(pady=10)
    
    # NOTE EDITOR SCREEN
    def show_note_screen(self, folder_name, note_name):
        """Show note editor screen"""
        self.clear_window()
        self.current_folder = folder_name
        self.current_note = note_name
        
        # Load note content
        note_path = os.path.join(self.notes_folder, folder_name, f"{note_name}.txt")
        with open(note_path, "r") as f:
            content = f.read()
        
        # Title
        title = tk.Label(
            self.root,
            text=f"Note: {note_name}",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)
        
        # Text area for editing
        text_area = tk.Text(self.root, height=15, width=60, font=("Arial", 10))
        text_area.pack(pady=10, padx=10)
        text_area.insert("1.0", content)
        
        # Button frame for actions
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        # Save button
        def save_changes():
            new_content = text_area.get("1.0", tk.END)
            with open(note_path, "w") as f:
                f.write(new_content)
            messagebox.showinfo("Success", "Note saved successfully")
        
        save_btn = tk.Button(
            button_frame,
            text="Save",
            image=self.icons.get('save'),
            compound='left',
            font=("Arial", 10),
            command=save_changes
        )
        save_btn.pack(side=tk.LEFT, padx=5)
        
        # Delete button
        def delete_note():
            result = messagebox.askyesno("Confirm", "Delete this note?")
            if result:
                os.remove(note_path)
                messagebox.showinfo("Success", "Note deleted")
                self.show_notes_in_folder(folder_name)
        
        delete_btn = tk.Button(
            button_frame,
            text="Delete",
            image=self.icons.get('delete'),
            compound='left',
            font=("Arial", 10),
            command=delete_note
        )
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Export button
        def export_note():
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w") as f:
                    f.write(text_area.get("1.0", tk.END))
                messagebox.showinfo("Success", f"Note exported to {file_path}")
        
        export_btn = tk.Button(
            button_frame,
            text="Export",
            image=self.icons.get('export'),
            compound='left',
            font=("Arial", 10),
            command=export_note
        )
        export_btn.pack(side=tk.LEFT, padx=5)
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="Back",
            image=self.icons.get('back'),
            compound='left',
            font=("Arial", 10),
            command=lambda: self.show_notes_in_folder(folder_name)
        )
        back_btn.pack(pady=5)
    
    # HELPER FUNCTIONS
    def get_folders(self):
        """Get list of all folders in notes directory"""
        folders = []
        for item in os.listdir(self.notes_folder):
            path = os.path.join(self.notes_folder, item)
            if os.path.isdir(path):
                folders.append(item)
        
        if not folders:
            # Create default folder
            os.makedirs(os.path.join(self.notes_folder, "General"))
            folders.append("General")
        
        return sorted(folders)
    
    def get_notes_in_folder(self, folder_path):
        """Get list of all notes in a folder"""
        notes = []
        if os.path.exists(folder_path):
            for item in os.listdir(folder_path):
                if item.endswith(".txt"):
                    notes.append(item)
        return sorted(notes)


# Import for askstring
import tkinter.simpledialog

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
