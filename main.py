import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("main_customtkinter")
root.geometry("600x600")

# pack()
frame = customtkinter.CTkFrame(master=root, fg_color="yellow", bg_color="yellow" )
frame.pack(side='left', expand=True, fill='both')

frame2 = customtkinter.CTkFrame(master=root, fg_color="blue", bg_color="blue" )
frame2.pack(side='bottom', expand=True, fill='both')
# place() - 0.1 -> 10%
frame3 = customtkinter.CTkFrame(master=root, fg_color="red", bg_color="red" )
frame3.place(relwidth = 1, relheight = 1 ,relx=0.5, rely=0.5)
# grid()

root.mainloop()