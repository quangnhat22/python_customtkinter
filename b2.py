import customtkinter

customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title("b2_pack")
root.geometry("600x600")

top_frame = customtkinter.CTkFrame(root)
top_frame.pack(side="top", fill="both", expand=True)
bottom_frame = customtkinter.CTkFrame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True)

top_left_frame = customtkinter.CTkFrame(top_frame, fg_color="yellow", bg_color="yellow")
top_left_frame.pack(side="left", fill="both", expand=True)
top_right_frame = customtkinter.CTkFrame(top_frame, fg_color="red", bg_color="yellow")
top_right_frame.pack(side="right", fill="both", expand=True)

bottom_left_frame = customtkinter.CTkFrame(bottom_frame, fg_color="grey", bg_color="grey")
bottom_left_frame.pack(side="left", fill="both", expand=True)
bottom_right_frame = customtkinter.CTkFrame(bottom_frame, fg_color="blue", bg_color="blue")
bottom_right_frame.pack(side="right", fill="both", expand=True)

root.mainloop()