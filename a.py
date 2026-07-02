from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import threading
import time

class BirthdayCardServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # --- CUSTOMIZE YOUR VISION HERE (DARK EMERALD THEME) ---
        background_color = "#0A1F16"  # Deep, moody dark emerald night background
        envelope_color = "#123024"    # Dark velvet emerald for the outer envelope
        paper_color = "#1B4D3E"       # Slightly lighter emerald for the internal letter paper
        text_color = "#E0F2F1"        # Luminous mint-white for crisp, glowing text
        accent_color = "#00C853"      # Vivid, neon emerald green for highlights
        
        # Make this as long as you want! It will automatically scroll.
        birthday_message = """
        Dearest Friend,<br><br>
        Happy Birthday! This is a space where you can write an incredibly long, deep message. Because the paper has a fixed height and dynamic scrolling built into it, you never have to worry about running out of space.<br><br>
        You can talk about your favorite memories together, share jokes, list out the reasons you appreciate them, or outline wishes for their upcoming year.<br><br>
        Scroll down to keep reading...<br><br>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br><br>
        End of the letter. I hope your day is as magical as this card!
        """
        # --------------------------------------------------------

        html_layout = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Happy Birthday!</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Pacifico&display=swap" rel="stylesheet">
            
            <style>
                body {{
                    background-color: {background_color};
                    font-family: "Fredoka", sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    min-height: 100vh;
                    overflow: hidden;
                }}

                h1 {{
                    font-family: "Pacifico", cursive;
                    color: {accent_color};
                    font-size: 2.5rem;
                    margin-bottom: 40px;
                    text-shadow: 0 0 10px rgba(0, 200, 83, 0.3);
                    z-index: 10;
                    transition: opacity 0.5s ease;
                }}

                /* The Interactive Envelope System */
                .envelope-wrapper {{
                    position: relative;
                    width: 450px;
                    height: 300px;
                    background-color: {envelope_color};
                    border-radius: 0 0 15px 15px;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 30px rgba(0, 200, 83, 0.1);
                    cursor: pointer;
                    display: flex;
                    justify-content: center;
                    z-index: 5;
                }}

                /* The Envelope Triangle Flap */
                .envelope-wrapper::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    width: 0;
                    height: 0;
                    border-left: 225px solid transparent;
                    border-right: 225px solid transparent;
                    border-top: 150px solid {envelope_color}; /* Matches envelope color */
                    transform-origin: top;
                    transition: transform 0.6s ease-in-out, z-index 0.2s ease-in-out 0.2s;
                    z-index: 6;
                    filter: drop-shadow(0px 5px 5px rgba(0,0,0,0.3));
                }}

                /* Hint text overlaid on the sealed envelope */
                .click-hint {{
                    position: absolute;
                    top: 50%;
                    color: {accent_color};
                    font-weight: bold;
                    font-size: 1.2rem;
                    z-index: 7;
                    pointer-events: none;
                    transition: opacity 0.3s ease;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                }}

                /* The Inside Paper Letter */
                .letter-paper {{
                    position: absolute;
                    top: 20px;
                    width: 400px;
                    height: 240px;
                    background-color: {paper_color};
                    border: 2px solid {accent_color};
                    border-radius: 10px;
                    padding: 25px;
                    box-sizing: border-box;
                    overflow-y: auto; /* Enables vertical scrolling */
                    color: {text_color};
                    transition: transform 0.8s ease-in-out 0.4s, height 0.6s ease-in-out 1s;
                    z-index: 2;
                    box-shadow: inset 0 0 20px rgba(0,0,0,0.3);
                }}

                /* Custom Scrollbar styling for a smooth green aesthetic */
                .letter-paper::-webkit-scrollbar {{
                    width: 8px;
                }}
                .letter-paper::-webkit-scrollbar-thumb {{
                    background: {accent_color};
                    border-radius: 10px;
                }}

                /* --- OPEN STATE ANIMATIONS --- */
                /* When clicked, we add the "open" class via Python's embedded script */
                
                /* 1. Flip the top flap up */
                .envelope-wrapper.open::before {{
                    transform: rotateX(180deg);
                    z-index: 1; /* Move behind paper after flipping */
                }}

                /* 2. Slide the paper UP out of the envelope and expand its height */
                .envelope-wrapper.open .letter-paper {{
                    transform: translateY(-220px);
                    height: 450px; 
                    z-index: 8; /* Bring paper to the very front so user can scroll it */
                }}

                /* 3. Hide the click instructions */
                .envelope-wrapper.open .click-hint {{
                    opacity: 0;
                }}
            </style>
        </head>
        <body>

            <h1 id="title-text">You have an unread letter...</h1>

            <div class="envelope-wrapper" onclick="openEnvelope(this)">
                <div class="click-hint">Click to Open ✉️</div>
                
                <div class="letter-paper" onclick="event.stopPropagation();">
                    {birthday_message}
                </div>
            </div>

            <script>
                function openEnvelope(element) {{
                    // Add the class that triggers all CSS transitions at once
                    element.classList.add('open');
                    document.getElementById('title-text').innerText = "Happy Birthday! 🎉";
                }}
            </script>

        </body>
        </html>
        """
        self.wfile.write(bytes(html_layout, "utf-8"))

def open_edge():
    time.sleep(1) 
    print("Opening your Animated Birthday Letter in Edge...")
    webbrowser.open("http://localhost:8000")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, BirthdayCardServer)
    threading.Thread(target=open_edge).start()
    httpd.serve_forever()

if __name__ == '__main__':
    run()
