#this needs tksheet to be installed.
#pip3 install tksheet
import tkinter as tk
import tksheet


top = tk.Tk()
sheet = tksheet.Sheet(top)
sheet.grid()
data = ["datasheet"]

sheet.set_sheet_data(
    [
        #[f"{ri+cj}" for cj in range(4)]
        [f"{data[0]}" for cj in range(4)]
        for ri in range(4)
    ]
)

#table enable choices listed below:
sheet.enable_bindings(
    (
        "row_select",
        "column_width_resize",
        "arrowkeys",
        "right_click_popup_menu",
        "rc_select",
        "rc_insert_row",
        "rc_delete_row",
        "copy",
        "cut",
        "paste",
        "delete",
        "undo",
        "edit_cell"
    )
)

top.mainloop()