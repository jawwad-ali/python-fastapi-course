# Voice Appointment Agent

## 🎯 Goal

Build a voice agent that takes an appointment request over a conversation and
saves it.

## 🛠️ Requirements

- A voice conversation the caller can hold
- The customer's name, collected by voice
- The customer's preferred date and time
- An availability check
- A spoken confirmation
- The appointment stored somewhere

## 💪 Tasks

1. Create a Google Sheet with columns: `name`, `date`, `time`, `status`.
2. Build an n8n webhook workflow that receives a name, a date and a time.
3. In that workflow, check the sheet for a row that already has the same date and
   time.
4. If the slot is free, add the row and reply `booked`. If it is taken, reply
   `busy` and suggest a different time.
5. Create the voice agent. Its system prompt must tell it to ask for the name
   first, then the date, then the time — one question at a time.
6. Connect the workflow as a tool with three parameters: name, date and time.

## ✅ Done When

- You can book an appointment entirely by voice and see the new row in the sheet.
- Booking the same slot twice makes the agent offer a different time.
- The agent repeats the details back before saving, so the caller can correct it.
