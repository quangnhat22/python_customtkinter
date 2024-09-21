import customtkinter

customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title("b3_pack")
root.geometry("600x600")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

top_left_frame = customtkinter.CTkFrame(root, fg_color="yellow", bg_color="yellow")
top_left_frame.grid(row=0, column=0, sticky="nsew")
top_right_frame = customtkinter.CTkFrame(root, fg_color="red", bg_color="yellow")
top_right_frame.grid(row=0, column=1, sticky="nsew")

bottom_left_frame = customtkinter.CTkFrame(root, fg_color="grey", bg_color="grey")
bottom_left_frame.grid(row=1, column=0, sticky="nsew")
bottom_right_frame = customtkinter.CTkFrame(root, fg_color="blue", bg_color="blue")
bottom_right_frame.grid(row=1, column=1, sticky="nsew")

root.mainloop()