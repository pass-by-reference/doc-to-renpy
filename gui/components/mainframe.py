from tkinter import PhotoImage, StringVar, Listbox, Text, messagebox
from tkinter import N, S, E, W, SINGLE, SEL, INSERT
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile
from gui.user.state import State
from gui.user.document import Document, DocumentStatus

from gui.constants import BASE_PATH

def get_name_from_path(path : str) -> str:
  path_parts = path.rsplit("/")
  last_index = len(path_parts) - 1

  return path_parts[last_index]

class MainFrame:
  def __init__(self, root, state : State):
    self.__init_images()
    self.__init_widgets(root)
    self.__init_bind_widgets()
    self.__init_configure_grid()
    self.__init_configure_col_row_weights()

    self.state = state
    # self.state.load(self.choice_var)

    self.convert_button.grid_forget()
    self.delete_button.grid_forget()
    self.download_rpy_button.grid_forget()

  def __init_images(self):
    self.open_image = PhotoImage(file="{0}/assets/add.png".format(BASE_PATH))
    self.convert_image = PhotoImage(file="{0}/assets/convert.png".format(BASE_PATH))
    self.delete_image = PhotoImage(file="{0}/assets/delete.png".format(BASE_PATH))
    self.download_rpy_image = PhotoImage(file="{0}/assets/download.png".format(BASE_PATH))

  def __init_widgets(self, root):
    self.mainframe = ttk.Frame(root, padding=(12,12,12,12))
  
    self.toolbar = ttk.Frame(self.mainframe)
    self.left_toolbar = ttk.Frame(self.toolbar)
    self.open_button = ttk.Button(self.left_toolbar, image=self.open_image, width=2, command=self.open_file)
    
    self.right_toolbar = ttk.Frame(self.toolbar)
    self.convert_button = ttk.Button(self.right_toolbar, image=self.convert_image, width=2, command=self.convert)
    self.delete_button = ttk.Button(self.right_toolbar, image=self.delete_image, width=2, command=self.delete)

    self.download_rpy_button = ttk.Button(self.mainframe, image=self.download_rpy_image, command=self.save_rpy_file)
    
    self.docx_frame = ttk.Frame(self.mainframe, relief="ridge")
    self.choice_var = StringVar(value=[])
    self.choicebox = Listbox(self.docx_frame, height=30, listvariable=self.choice_var, selectmode=SINGLE)

    self.rpy_frame = ttk.Frame(self.mainframe, relief="ridge")
    self.rpy_text = Text(self.rpy_frame, relief="ridge")
    self.rpy_text.tag_add('select-all', '1.0', 'end')

  def __init_bind_widgets(self):
    self.choicebox.bind("<<ListboxSelect>>", self.change_selection)
    self.choicebox.bind("<Double-1>", self.change_selection)
    
    self.rpy_text.bind("<Double-Button-1>", self.choice_box_deselect)
    self.rpy_text.bind("<Control-a>", self.renpy_text_select_all)

  def __init_configure_grid(self):
    self.mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

    self.toolbar.grid(column=0, row=0, rowspan=1, sticky=(N, S, E, W), padx=5)
    self.left_toolbar.grid(column=0, row=0, sticky=(N, S, E, W))
    self.right_toolbar.grid(column=1, row=0, sticky=(N, S, E, W))

    self.open_button.grid(column=0, row=0, columnspan=1, sticky=(N, S))
    # self.convert_button.grid(column=2, row=0, columnspan=1, rowspan=1, sticky=(N, S), padx=3)
    # self.delete_button.grid(column=3, row=0, columnspan=1,rowspan=1, sticky=(N, S), padx=3)

    self.docx_frame.grid(column=0, row=1, columnspan=1, rowspan=1, sticky=(N, S, E, W), pady=5, padx=5)
    self.choicebox.grid(column=0, row=0, sticky=(N, S, E, W))

    self.rpy_frame.grid(column=1, row=1, columnspan=1, rowspan=2, sticky=(N, S, E, W), pady=5, padx=5)
    self.rpy_text.grid(column=0, row=0, sticky=(N, S, E, W))
    # self.download_rpy_button.grid(column=1, row=0, columnspan=1, rowspan=1, sticky=(W), padx=5)

  def __init_configure_col_row_weights(self):
    self.mainframe.columnconfigure(0, weight=1)
    self.mainframe.columnconfigure(1, weight=1)
    self.mainframe.columnconfigure(2, weight=1)
    self.mainframe.rowconfigure(0, weight=1)
    self.mainframe.rowconfigure(1, weight=5)

    self.toolbar.columnconfigure(0, weight=1)
    self.toolbar.columnconfigure(1, weight=1)
    self.toolbar.rowconfigure(0, weight=1)

    self.right_toolbar.columnconfigure(0, weight=1)
    self.right_toolbar.columnconfigure(1, weight=1)
    self.right_toolbar.columnconfigure(2, weight=1)
    self.right_toolbar.columnconfigure(3, weight=1)
    self.right_toolbar.rowconfigure(0, weight=1)

    self.docx_frame.columnconfigure(0, weight=1)
    self.docx_frame.rowconfigure(0, weight=1)

    self.rpy_frame.columnconfigure(0, weight=1)
    self.rpy_frame.rowconfigure(0, weight=1)

  def get_name_from_path(path : str) -> str:
    path_parts = path.rsplit("/")
    last_index = len(path_parts) - 1

    return path_parts[last_index]

  def open_file(self):
    file = askopenfile(mode='r', filetypes=[("Word Document 2007", ".docx")])
    if file is not None:

      filename = get_name_from_path(file.name)

      if self.state.does_file_name_exist(filename):
        
        can_replace_file : bool = messagebox.askokcancel("Warning", 
          "This file exists. Do you want to replace it?",
          icon = "warning"
        )

        if(can_replace_file):
          document = self.state.get_document(filename)
          document.overwrite(filename)

          self.change_selection(None)

        return
      
      document = Document(file.name)
      self.state.doc_list.append(document)
      self.choice_var.set(self.state.doc_list)

  def change_selection(self, event):
    selection : tuple = self.choicebox.curselection() # Returns a tuple of index of selected listbox item
    if(len(selection) > 0 and 
      selection[0] < len(self.state.doc_list) # Grab the first element in tuple
    ):
      index = selection[0]

      self.convert_button.grid(column=2, row=0, columnspan=1, rowspan=1, sticky=(N, S, E, W), padx=3)
      self.delete_button.grid(column=3, row=0, columnspan=1,rowspan=1, sticky=(N, S, E, W), padx=3)
      
      document : Document = self.state.doc_list[index]

      if(document.status == DocumentStatus.CONVERTED):
        self.download_rpy_button.grid(column=1, row=0, columnspan=1, rowspan=1, sticky=(W), padx=5)

      text : str = document.on_select()
      self.rpy_text.delete("1.0", "end")
      self.rpy_text.insert("1.0", text)
  
  def choice_box_deselect(self, event):
    self.convert_button.grid_forget()
    self.delete_button.grid_forget()
    self.download_rpy_button.grid_forget()

  def convert(self):
    selection : tuple = self.choicebox.curselection() # Returns a tuple of index of selected listbox item
    if(len(selection) > 0 and 
      selection[0] < len(self.state.doc_list) # Grab the first element in tuple
    ):
      index = selection[0]

      document : Document = self.state.doc_list[index]
      # Already converted
      if document.status == DocumentStatus.CONVERTED:
        return

      document.convert()
      self.change_selection(None)

  def delete(self):
    selection : tuple = self.choicebox.curselection() # Returns a tuple of index of selected listbox item
    if(len(selection) > 0 and 
      selection[0] < len(self.state.doc_list) # Grab the first element in tuple
    ):
      index = selection[0]
      document : Document = self.state.doc_list[index]
      document.remove_files()
      self.state.doc_list.remove(document)
      self.choice_var.set(self.state.doc_list)

      self.convert_button.grid_forget()
      self.delete_button.grid_forget()
      self.download_rpy_button.grid_forget()

    if(len(self.state.doc_list) == 0):
      self.rpy_text.delete("1.0", "end")

  def save_rpy_file(self):
    selection : tuple = self.choicebox.curselection() # Returns a tuple of index of selected listbox item
    if(len(selection) > 0 and 
      selection[0] < len(self.state.doc_list) # Grab the first element in tuple
    ):
      index = selection[0]
      document : Document = self.state.doc_list[index]

      if document.status == DocumentStatus.CONVERTED:
        file = asksaveasfile(filetypes=[("renpy script format", ".rpy")])
        if not file:
          # Cancelled request
          return

        try:
          read_file = open(document.renpy_file_path, "r")
        except FileNotFoundError:
          print("Save_rpy_file: Cannot find rpy file to write")
          return

        file.write(read_file.read())
  
  def renpy_text_select_all(self, event):

    self.rpy_text.tag_add(SEL, "1.0", "end")
    self.rpy_text.mark_set(INSERT, "1.0")
    self.rpy_text.see(INSERT)

    return "break"