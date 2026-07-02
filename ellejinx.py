from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import threading
import time
import os
import urllib.parse  # Added to handle file names with spaces

class BirthdayCardServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # --- LOCAL FILE ROUTING MAP ---
        # urllib.parse.unquote changes things like "%20" back into real spaces
        file_path = urllib.parse.unquote(self.path.strip("/"))
        
        if file_path.endswith((".mp3", ".png", ".jpg", ".jpeg")):
            if os.path.exists(file_path):
                self.send_response(200)
                if file_path.endswith(".mp3"):
                    self.send_header('Content-type', 'audio/mpeg')
                elif file_path.endswith(".png"):
                    self.send_header('Content-type', 'image/png')
                else:
                    self.send_header('Content-type', 'image/jpeg')
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_error(404, f"File Not Found: {file_path}")
                return

        # Main page delivery
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.end_headers()
        
        # --- THE DESIGN VARIABLES ---
        background_color = "#0A1F16"  
        envelope_color = "#123024"    
        paper_color = "#1B4D3E"       
        text_color = "#E0F2F1"        
        accent_color = "#00C853"      
        pin_code = "46854"
        birthday_message = """hello bbg. HAPPY BIRTHDAYYYYY!!! my nigga u r now the same age as me. so u cant be talking abt some, u r unc. u cant say that to me anymore. but what u can do is read this long ass literal essay abt why i am so happy to have known u and see u turn 19. 

there is a tldr at the bottom if you want.


im writing this wayyyyyyyy earlier than ur actual birthday date. idk but i just heard ur vm and it made me really emotional and im like why not keep the momentum up and write her birthday letter when i am in my emotional state bc thats when i am mostly myself; true and authentic, corny and a nigga, no second guessing what i say and a black muslim. and that’s why i wanted to write this now. i’m usually closed off but u deserve real real. u the real goat. so just know everything i say here rn, i genuinely mean it. ofc i mean what i say when i talk to u, unless it’s me saying i hate u or calling u jewish slurs, but today idk it’s different. i’m going to unapologetically write exactly what’s going on thru my head. i am also listening to my locked up emotional, yearning playlist rn. so know this is RAWWWWW. and i’m sure one of these songs rn going to stick and make me remember u each time i hear it. 
okay this is future me here.

i’m listening to the playlist and i found ur song. it’s calla by wave to earth. i will explain later why this stuck to me.

so im going to write every instance that stuck to me and then glaze you so bad that it is enough to give a hungry kid in africa diabeties.

yeah today you told me that words of affirmation is something i needed. and that’s so true. i always doubt that im not good enough of a friend so i distance myself bc being closer with someone then losing them is much more scarier than being alone. ik that holds me back from fully creating genuine connections with you. i hate myself for that, but i can’t help it. i just do. my fucking on and offs. but want i want you to know is that even through all of that you still talk to me. and most of all, i never had to explain why i distance myself like that. and yet you seem to know that i do that when somethings going on. and you don’t take it personally. thank you. you don’t make me feel stupid for being human and coping to things the way i have known. you are literally me but in a different body and lived across the globe. thank you for giving me the benefit of the doubt. you are consistent with that. and that understanding is something you are really good at, no glaze guys.

i am not some one who opens up that easily. it takes years to even talk abt anything abt myself. i feel like ppl hate that but if you are not safe for me or curious abt me, i would rather not. even if it’s the need is still always there. like opening up with someone, it just feels like im stripping naked in front of 50 ppl and all that for some random ass nigga to say why your bush clean. (idek where u was headed with that but yeah) i’m just trying to plead my case here. 

and from there i’m going to bring it to the fact that looking at you heals me. like you are genuinely a gorgeous ass skinny queen mf. SKINNYYY. i know that for sure. like i don’t even have to say anything abt it. i love your green eyes. guys that is literal emerald eyes. they are such a beautiful shade. i’ve wanted eyes like yours. i love the short stands of hair you have at front. because you can never seem to tie them up and they always annoy you when you walk, but it makes me laugh. your skin is to die for. you have such silky smooth ass skin i love that you experiment with your eyebrows because why not guys. when you have ones like that it would be a waste not to (and no i wasn’t analyzing your pretty face when we talk). i’m so sure that anyone that has a chance to see what i saw is a lucky person. im
talking about you as a person in and out btw. 

like you are such an imperfect perfect human being. you make mistakes and you can’t be completely perfect on everything you do for yourself and others. obviously. but like as a human being, knowing what you have been through, i don’t think someone can still be like this. still understanding, still empathetic, not racist (debatable), judges someone based off character and not looks, sharing, physical only with people you love, observant, and a little giggleshit. i swear i always hear your laugh when i say giggle shit. and also because we laugh the exact same way, and i am always reminded of that when i laugh. it’s a nice little thing to think abt when im across the world no? 

yeah as i was saying looking at you heals me. you are so confident now. i love how you are so care free. so strict when it comes to your boundaries. and selfish at times. i mean that in the most admiring way possible. knowing that you used to be like me, and now this is the person you have become gives me hope that i can also be like that. so know i always look up to you. 

and most of all, everyone around me knows about you. the specific word i use is that you feel like a sister to me. honestly speaking, i never thought i would call someone who isn’t blood related to me a sister. not even my high school friends are like that. i have good friends, but it’s just not the same. i’m just trying to stress that whenever you call me a sister it means so much to me. and whenever i call you my sister, it’s because i fight with you all the time, physically and verbally, talk to you almost everyday, know what is going on most of the time, and full heartedly fear that i wouldn’t be the same person if you were ever to leave my life. 

and to close this off. i just want to share some of my concerns because i care about you. but i still understand that i don’t know the full picture and i would love for you to explain them for me if there are any. 

i want you to take care of yourself physically. i knowwwww. i don’t want to be another parent on your ear. or an annoying parrot. but i don’t want you dropping dead on me either. i know there might not be any appetite but like. what can i do i know. but i still want you eating and alive. do you want to bake and make our own foods from scratch next year?? i would be down honestly. i need to get my ass in the kitchen and know how to make food anyway. 

and you reach to me when you are stressed and down or need someone to lend and ear to. I love that you choose me to reach out to but i noticed that i don’t do much. i piss myself off a lot bc of that. i remember you throwing up because you drank too much on the game with manny and you called me. i don’t drink so i wouldn’t know how to help. i’m so bad at comforting. i don’t seem to know what to say the way you do. but what i can do is be a consistent annoying presence if you need me to. i can do that. sooo yeah. 

 
yeah i love you too. I know I know. 
and can you please clock me the next time you feel like it. tell me that i annoying you and you actually mean it. but also tell me what i did wrong. so that i can learn. 

ohhhh and the song i said that now reminds me of u each time i listen to it. it’s calla by wave to earth. let me give you context. so wave to earth are my top 3 most listened to artist in my lifetime. my friends know that when wave to earth is mentioned it means i’m spawning either in three seconds or they are talking about me. i am one with wave to earth. i love them so much to the point that their songs are going to be played at my wedding. i want to collected their vinyls when i have money and i want to buy their lego album  and i want to go to their concert. OMDSSSSSS BRO LIKE I BOUGHT THEIR TICKETS JUST NOW. I BOUGHT THE TICKETS. BRO CAN YOU HEAR ME I BOUGHT THE TICKETS. IM GOING IN SEPTEMBER. NO OCT. ANYWAY I LOVE THEM SO MUCH. i have cried and slept to their songs and my sister and dagim have written letters to me that features wave to earth. okay now that we have context out of the way, why calla. the lyrics literally says i don’t want this to be a daydream. i want you to be real because at times you are too good to be true. then it says, someone said that your time will be over soon. i am a hard believer that all good things must come to an end.

the white rabbit has traumatized me for life and i hate it. and i hate to think that there would be a time that we aren’t close the way we are right now. but you can always grow back. if you don’t have enough sunlight i will blow the clouds away for you. it’s like saying no matter what happens i will be there for you and help you grow. and you actually do. whenever i am with you i don’t seem to care what other people think. you blow the social anxiety away for me. and you watch me grow. so there you go my analysis for the song calla and why it reminds me of you now. and for rest of my life too. this is phenomenal chat.

TLDR
FUCK U NIGGA YOU ARE READING THE ENTIRE THING IDGAF."""



        # --- REBUILT HTML BLOCKS TO PREVENT INTERPOLATION ERRORS ---
        html_layout = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Happy Birthday!</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Pacifico&display=swap" rel="stylesheet">
            
            <style>
                body {
                    background-color: BG_COLOR;
                    font-family: "Fredoka", sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    min-height: 100vh;
                    overflow: hidden;
                    position: relative;
                }

                #pin-overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    background-color: BG_COLOR;
                    z-index: 1000;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    transition: opacity 0.5s ease-out, visibility 0.5s;
                }

                .pin-box {
                    background-color: ENV_COLOR;
                    padding: 40px;
                    border-radius: 20px;
                    border: 1px solid rgba(0, 200, 83, 0.2);
                    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
                    text-align: center;
                    width: 320px;
                }

                .pin-box h2 {
                    color: TXT_COLOR;
                    margin-top: 0;
                    margin-bottom: 25px;
                    font-size: 1.4rem;
                    letter-spacing: 1px;
                }

                .pin-input-container {
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 25px;
                }

                .pin-digit {
                    width: 40px;
                    height: 50px;
                    background-color: BG_COLOR;
                    border: 2px solid rgba(224, 242, 241, 0.2);
                    border-radius: 8px;
                    text-align: center;
                    font-size: 1.5rem;
                    color: ACCENT_COLOR;
                    font-weight: bold;
                }

                .pin-digit:focus {
                    border-color: ACCENT_COLOR;
                    outline: none;
                    box-shadow: 0 0 10px rgba(0, 200, 83, 0.3);
                }

                #error-msg {
                    color: #ff5252;
                    font-size: 0.9rem;
                    min-height: 20px;
                    margin: 0;
                }

                h1 {
                    font-family: "Pacifico", cursive;
                    color: ACCENT_COLOR;
                    font-size: 2.5rem;
                    margin-bottom: 80px;
                    text-shadow: 0 0 10px rgba(0, 200, 83, 0.3);
                    z-index: 10;
                }

                .card-viewport {
                    position: relative;
                    width: 450px;
                    height: 350px; 
                    display: flex;
                    align-items: flex-end; 
                }

                .envelope-wrapper {
                    position: relative;
                    width: 450px;
                    height: 300px;
                    background-color: ENV_COLOR;
                    border-radius: 0 0 15px 15px;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
                    cursor: pointer;
                    z-index: 5;
                }

                .envelope-wrapper::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    width: 0;
                    height: 0;
                    border-left: 225px solid transparent;
                    border-right: 225px solid transparent;
                    border-top: 150px solid ENV_COLOR; 
                    transform-origin: top;
                    transition: transform 0.4s ease-in-out;
                    z-index: 6;
                }

                .click-hint {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    color: ACCENT_COLOR;
                    font-weight: bold;
                    font-size: 1.2rem;
                    z-index: 7;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    transition: opacity 0.3s;
                }
                
                .instagram-music-wrapper {
                    position: absolute;
                    top: 25px;
                    right: 25px;
                    display: flex;
                    flex-direction: column;
                    align-items: flex-end;
                    gap: 8px;
                    z-index: 100;
                }

                .music-select-dropdown {
                    background: rgba(18, 48, 36, 0.95);
                    border: 1px solid rgba(0, 200, 83, 0.3);
                    border-radius: 12px;
                    color: TXT_COLOR;
                    font-family: "Fredoka", sans-serif;
                    padding: 8px;
                    font-size: 0.85rem;
                    outline: none;
                    cursor: pointer;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
                    backdrop-filter: blur(10px);
                    width: 100%;
                    box-sizing: border-box;
                    transition: opacity 0.3s, transform 0.3s;
                }

                .instagram-music-container {
                    display: flex;
                    align-items: center;
                    background: rgba(18, 48, 36, 0.6);
                    padding: 10px 18px 10px 10px;
                    border-radius: 50px;
                    backdrop-filter: blur(8px);
                    border: 1px solid rgba(0, 200, 83, 0.2);
                    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
                    cursor: pointer;
                    position: relative;
                }

                .album-art-wrapper {
                    position: relative;
                    width: 60px;
                    height: 60px;
                }

                .album-cover {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 60px;
                    height: 60px;
                    border-radius: 6px;
                    z-index: 12;
                    object-fit: cover;
                    box-shadow: 3px 0 10px rgba(0,0,0,0.3);
                }

                .vinyl-disk {
                    position: absolute;
                    top: 3px;
                    left: 20px; 
                    width: 54px;
                    height: 54px;
                    background: radial-gradient(circle, #050505 30%, #222 31%, #050505 40%, #111 60%, #050505 70%);
                    border-radius: 50%;
                    z-index: 11;
                    transition: left 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                    border: 1px dashed rgba(255,255,255,0.05);
                }

                .vinyl-disk::after {
                    content: '';
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    width: 10px;
                    height: 10px;
                    background-color: PAPER_COLOR;
                    border-radius: 50%;
                    border: 2px solid #050505;
                }

                .instagram-music-container.playing .vinyl-disk {
                    left: 32px; 
                    animation: spinDisk 3.5s linear infinite;
                }

                @keyframes spinDisk {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }

                .track-details {
                    margin-left: 45px; 
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    pointer-events: none;
                    padding-right: 25px;
                }

                .music-select-dropdown option {
                    background: ENV_COLOR;
                    color: TXT_COLOR;
                    padding: 6px;
                }

                .music-hint-tooltip {
                    position: absolute;
                    bottom: -80px;
                    right: 20px;
                    background-color: ACCENT_COLOR;
                    color: #050505;
                    font-size: 0.8rem;
                    font-weight: 600;
                    padding: 6px 14px;
                    border-radius: 20px;
                    white-space: nowrap;
                    box-shadow: 0 6px 15px rgba(0, 200, 83, 0.4);
                    pointer-events: none;
                    opacity: 0;
                    transform: translateY(-5px);
                    transition: opacity 0.4s ease, transform 0.4s ease;
                    z-index: 150;
                }

                .music-hint-tooltip::before {
                    content: '';
                    position: absolute;
                    top: -6px;
                    right: 35px;
                    border-width: 0 6px 6px 6px;
                    border-style: solid;
                    border-color: transparent transparent ACCENT_COLOR transparent;
                }

                .music-hint-tooltip.visible {
                    opacity: 1;
                    transform: translateY(0);
                }

                .letter-paper {
                    position: absolute;
                    bottom: 0px; 
                    left: 25px;
                    width: 400px;
                    height: 380px; 
                    background-color: PAPER_COLOR;
                    border: 2px solid ACCENT_COLOR;
                    border-radius: 10px;
                    padding: 25px;
                    box-sizing: border-box;
                    overflow-y: auto; 
                    color: TXT_COLOR;
                    opacity: 0; 
                    transition: transform 0.6s ease-in-out 0.2s, opacity 0.4s ease-in-out 0.2s; 
                    z-index: 2;
                    white-space: pre-wrap;
                }

                .letter-paper::-webkit-scrollbar { width: 6px; }
                .letter-paper::-webkit-scrollbar-thumb { background: ACCENT_COLOR; border-radius: 10px; }

                .envelope-wrapper.open::before {
                    transform: rotateX(180deg);
                    z-index: 1; 
                }

                .envelope-wrapper.open .letter-paper {
                    opacity: 1;
                    z-index: 8; 
                    animation: liftAndSettle 1.4s ease-in-out forwards;
                }

                @keyframes liftAndSettle {
                    0% { transform: translateY(0); }
                    65% { transform: translateY(-200px); }
                    100% { transform: translateY(-20px); }
                }
            </style>
        </head>
        <body>
            
            <div id="pin-overlay">
                <div class="pin-box">
                    <h2>Enter Security Code</h2>
                    <div class="pin-input-container">
                        <input type="text" class="pin-digit" maxlength="1" oninput="moveNext(this, 0)" onkeydown="checkBack(event, 0)">
                        <input type="text" class="pin-digit" maxlength="1" oninput="moveNext(this, 1)" onkeydown="checkBack(event, 1)">
                        <input type="text" class="pin-digit" maxlength="1" oninput="moveNext(this, 2)" onkeydown="checkBack(event, 2)">
                        <input type="text" class="pin-digit" maxlength="1" oninput="moveNext(this, 3)" onkeydown="checkBack(event, 3)">
                        <input type="text" class="pin-digit" maxlength="1" oninput="moveNext(this, 4)" onkeydown="checkBack(event, 4)">
                    </div>
                    <p id="error-msg"></p>
                </div>
            </div>

            <audio id="bg-music" onended="autoNextTrack()"></audio>

            <div class="instagram-music-wrapper">
                <div id="music-widget" class="instagram-music-container" onclick="focusDropdown()">
                    <div class="album-art-wrapper">
                        <img id="display-cover" class="album-cover" src="/cover1.jpg" alt="Cover">
                        <div class="vinyl-disk"></div>
                    </div>
                    <div class="track-details">
                        <p id="display-title" style="margin:0; font-size:0.9rem; font-weight:600; color:TXT_COLOR; letter-spacing:0.5px;">Out Getting Ribs</p>
                        <p id="display-artist" style="margin:2px 0 0 0; font-size:0.75rem; color:ACCENT_COLOR; opacity:0.8;">Feeling Blew</p>
                    </div>
                    
                    <div id="hint-bubble" class="music-hint-tooltip">🎵 Click to change the song!</div>
                </div>

                <select id="track-dropdown" class="music-select-dropdown" onchange="selectTrack(this.value)">
                    <option value="0">Out Getting Ribs - Feeling Blew</option>
                    <option value="1">Moonlight - Chase Atlantic</option>
                    <option value="2">Calla - wave to earth</option>
                </select>
            </div>

            <h1 id="title-text">You have a letter sent by an owl... <br>(just like in harry potter)</h1>

            <div class="card-viewport">
                <div class="envelope-wrapper" onclick="openEnvelope(this)">
                    <div class="click-hint">Click to Open ✉️</div>
                    
                    <div class="letter-paper" onclick="event.stopPropagation();">B_DAY_MSG</div>
                </div>
            </div>

            <script>
                // FIXED: Moonlight now properly has its .mp3 extension mapping
                const playlist = [
                    { src: "out_getting_ribs.mp3", cover: "cover1.jpg", title: "Out Getting Ribs", artist: "Feeling Blew" },
                    { src: "moonlight.mp3", cover: "cover3.jpg", title: "Moonlight", artist: "Chase Atlantic" },
                    { src: "calla.mp3", cover: "cover2.jpg", title: "Calla", artist: "wave to earth" }
                ];
                
                let currentTrackIndex = 0;
                let appUnlocked = false;

                const music = document.getElementById('bg-music');
                const widget = document.getElementById('music-widget');
                const dropdown = document.getElementById('track-dropdown');
                const correctPin = "PIN_VAL";

                window.onload = () => {
                    document.querySelectorAll('.pin-digit')[0].focus();
                    music.src = playlist[currentTrackIndex].src;
                };

                function moveNext(input, index) {
                    if (input.value.length === 1 && index < 5) {
                        document.querySelectorAll('.pin-digit')[index + 1].focus();
                    }
                    verifyPinAssembly();
                }

                function checkBack(event, index) {
                    if (event.key === "Backspace" && !event.target.value && index > 0) {
                        document.querySelectorAll('.pin-digit')[index - 1].focus();
                    }
                }

                function verifyPinAssembly() {
                    const digits = document.querySelectorAll('.pin-digit');
                    let typedCode = "";
                    digits.forEach(d => typedCode += d.value);

                    if (typedCode.length === 5) {
                        if (typedCode === correctPin) {
                            appUnlocked = true;
                            document.getElementById('pin-overlay').style.opacity = '0';
                            setTimeout(() => {
                                document.getElementById('pin-overlay').style.visibility = 'hidden';
                                triggerMusicHint();
                            }, 500);
                            
                            playTrack();
                        } else {
                            document.getElementById('error-msg').innerText = "Incorrect Code. Try again.";
                            digits.forEach(d => d.value = "");
                            digits[0].focus();
                        }
                    }
                }

                function triggerMusicHint() {
                    const hint = document.getElementById('hint-bubble');
                    hint.classList.add('visible');
                    
                    setTimeout(() => {
                        hint.classList.remove('visible');
                    }, 4000);
                }

                // Focuses dropdown completely naturally when clicking widget token
                function focusDropdown() {
                    if (!appUnlocked) return;
                    dropdown.focus();
                }

                // Syncs UI displays effortlessly when tracks pivot
                function updateUIElements() {
                    document.getElementById('display-cover').src = playlist[currentTrackIndex].cover;
                    document.getElementById('display-title').innerText = playlist[currentTrackIndex].title;
                    document.getElementById('display-artist').innerText = playlist[currentTrackIndex].artist;
                    dropdown.value = currentTrackIndex;
                }

                function playTrack() {
                    music.src = playlist[currentTrackIndex].src;
                    music.load();
                    music.play().then(() => {
                        widget.classList.add('playing');
                    }).catch(err => console.log("Playback engine trace deferred"));
                }

                function selectTrack(index) {
                    if (!appUnlocked) return;
                    currentTrackIndex = parseInt(index);
                    updateUIElements();
                    playTrack();
                }

                function autoNextTrack() {
                    currentTrackIndex = (currentTrackIndex + 1) % playlist.length;
                    updateUIElements();
                    playTrack();
                }

                function openEnvelope(element) {
                    if (!appUnlocked) return;
                    if (!element.classList.contains('open')) {
                        element.classList.add('open');
                        document.getElementById('title-text').innerText = "Happy Birthday! 🎉";
                    }
                }
            </script>

        </body>
        </html>
        """

        # Safe programmatic replace to clean things up
        html_layout = html_layout.replace("BG_COLOR", background_color)
        html_layout = html_layout.replace("ENV_COLOR", envelope_color)
        html_layout = html_layout.replace("PAPER_COLOR", paper_color)
        html_layout = html_layout.replace("TXT_COLOR", text_color)
        html_layout = html_layout.replace("ACCENT_COLOR", accent_color)
        html_layout = html_layout.replace("PIN_VAL", pin_code)
        html_layout = html_layout.replace("B_DAY_MSG", birthday_message)

        self.wfile.write(bytes(html_layout, "utf-8"))

def open_edge():
    time.sleep(1) 
    print("Opening your Birthday Letter in Edge...")
    webbrowser.open("http://localhost:8000")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, BirthdayCardServer)
    threading.Thread(target=open_edge).start()
    httpd.serve_forever()

if __name__ == '__main__':
    run()
