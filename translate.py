import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("English to Turkish Sentence Game")

# Make the window full screen
root.attributes("-fullscreen", True)

# Add a function to exit full screen mode with "Escape"
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)
    root.quit()

title_label = tk.Label(root, text="Translate the following English sentences into Turkish.", font=("Arial", 24, "bold"))
title_label.pack(pady=30)
root.bind("<Escape>", exit_fullscreen)

# English sentences and their hidden Turkish translations
sentences = [
    ("I did not go to the party last night.", "Ben dün gece partiye gitmedim."),
    ("They visited the museum on the last school trip.", "Onlar son okul gezisinde müzeyi ziyaret ettiler."),
    ("Did you see the concert last night?", "Dün gece konseri gördün mü?"),
    ("She did not finish her homework.", "O ödevini bitirmedi."),
    ("Did she finish her book?", "O kitabını bitirdi mi?"),
    ("He helped his mother with the housework last weekend.", "O geçen hafta sonu annesine ev işlerinde yardım etti."),
    ("They did not watch the popular movie.", "Onlar popüler olan filmi izlemediler."),
    ("Did they travel to Italy last summer?", "Onlar geçen yaz İtalya'ya seyahat ettiler mi?"),
    ("We studied for exams together in the library last week.", "Biz geçen hafta kütüphanede birlikte sınavlara çalıştık."),
    ("He did not play soccer last week.", "O geçen hafta futbol oynamadı."),
    ("Did he call you yesterday?", "O dün seni aradı mı?"),
    ("We did not visit the museum.", "Biz müzeyi ziyaret etmedik."),
    ("Did he study for the exam yesterday?", "O dün sınav için çalıştı mı?"),
    ("You did not call me yesterday.", "Beni dün aramadın."),
    ("She read a book before bed last night.", "O dün gece yatmadan önce kitap okudu."),
    ("Did I leave my keys on the table?", "Anahtarlarımı masada mı unuttum?"),
    ("They traveled to different countries last year.", "Onlar geçen yıl farklı ülkelere seyahat ettiler."),
    ("Did you enjoy the vacation?", "Tatilin tadını çıkardın mı?"),
    ("We had lunch together last Sunday.", "Biz geçen pazar birlikte öğle yemeği yedik."),
    ("She took her dog for a walk yesterday.", "O dün köpeğini gezmeye çıkardı.")
]

# Calculate the longest Turkish word to dynamically set the placeholder width
longest_turkish_word = max(len(turkish) for _, turkish in sentences)

# Function to reveal the Turkish translation
def reveal_translation(label, translation):
    label.config(text=translation, fg="black")

# Create a frame to center the content
frame = tk.Frame(root)
frame.pack(expand=True)

# Loop through the sentences and create labels and buttons
for i, (english, turkish) in enumerate(sentences):
    # English sentence label
    english_label = tk.Label(frame, text=english, font=("Arial", 14), wraplength=600, justify="left")
    english_label.grid(row=i, column=0, padx=10, pady=2, sticky="w")
    
    # Placeholder sized based on the longest Turkish word
    # Placeholder sized based on the longest Turkish word with 10 extra stars
    placeholder = "*" * (longest_turkish_word + 13)
    turkish_label = tk.Label(frame, text=placeholder, font=("Arial", 14), fg="grey", anchor="w")
    turkish_label.grid(row=i, column=1, padx=20, pady=2, sticky="w")
    
    # Button to reveal the translation
    reveal_button = tk.Button(frame, text="Show", width=20, command=lambda l=turkish_label, t=turkish: reveal_translation(l, t))
    reveal_button.grid(row=i, column=2, padx=20, pady=2)

# Add the exit button at the bottom
exit_button = tk.Button(root, text="Exit", width=20, command=exit_fullscreen)
exit_button.pack(side="bottom", pady=20)


# Start the Tkinter main loop
root.mainloop()