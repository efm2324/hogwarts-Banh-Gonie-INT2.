def ask_text(message):
   while True:
      user_input = input(message).strip()
        if user_input:
            return user_input