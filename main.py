import openai
import tkinter as tk

# Set OpenAI API key
openai.api_key = "put your api key here mate "


# Function to fetch data from OpenAI and display it in a tkinter window
def display_openai_data():
    # Send request to OpenAI API
    response = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": "this is me , do i look health is there anything concerning? ?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://i.ibb.co/vmgNBFY/Screenshot-20240111-155807.jpg",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    # Get the output data message content
    data_message = response.choices[0].message.content

    # Create a tkinter window
    root = tk.Tk()
    root.title("Vision answer")

    # Create a text widget to display the output data message
    text_widget = tk.Text(root, height=50, width=50)
    text_widget.insert(tk.END, data_message)
    text_widget.pack(padx=50, pady=60)

    # Run the tkinter event loop
    root.mainloop()


# Call the display_openai_data function to fetch and display the output data message
display_openai_data()
