# Company Support Chatbot

## 🎯 Goal

Build a support chatbot that answers real customer questions from a company
document, and knows what to do when it does not have the answer.

## 📚 What You Will Build

- One company document with several policies in it
- A chatbot that answers customer questions from it
- A safe reply for questions the document does not cover

## 🛠️ Requirements

- A file called `company-policies.txt` in the `assets/` folder
- The same nodes as lesson 02
- Your free Google AI Studio API key

## 💪 Tasks

1. Create `company-policies.txt`. Write short, clear lines covering: returns,
   delivery, payment methods, support hours, and a contact email.
2. Build the insert workflow. Set **Memory Key** to `support` and run it.
3. Build the question workflow with the same Memory Key `support`.
4. Ask five questions a real customer would ask, such as
   *"Can I pay cash on delivery?"* Check every answer against your file.
5. Now ask something your document does **not** cover, such as
   *"Do you ship to Dubai?"* Notice what the chatbot does.
6. In the **Question and Answer Chain**, open **Options** and find the system
   prompt setting. Tell the model to reply with your support email when the
   answer is not in the documents.

## ✅ Done When

- All five customer questions are answered correctly from your file.
- The question you did not cover returns your support email, not a guess.
- A friend can ask it a question and get a useful reply without your help.
