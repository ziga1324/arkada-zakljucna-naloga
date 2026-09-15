import tkinter as tk
from tkinter import ttk

import random
import time

from network import ArcadeNetwork


class ArcadeSimulator:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Arcade Simulator"
        )

        self.root.geometry(
            "1000x650"
        )

        self.root.minsize(
            900,
            600
        )

        # -------------------------
        # NETWORK
        # -------------------------

        self.network = ArcadeNetwork(
            arcade_id="ARCADE-003",
            arcade_name="Main Arcade",
            software_version="0.1.0"
        )

        # -------------------------
        # ARCADE STATE
        # -------------------------

        self.arcade_online = False

        self.server_connected = False

        self.current_game = None

        self.players = 0

        self.temperature = 42.0

        self.cpu_usage = 20

        self.latency = 0

        self.heartbeat_count = 0

        # -------------------------

        self.create_ui()

        self.update_system()

    # =============================================
    # UI
    # =============================================

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="ARCADE MACHINE SIMULATOR",
            font=(
                "Arial",
                24,
                "bold"
            )
        )

        title.pack(
            pady=15
        )

        main_frame = tk.Frame(
            self.root
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # =====================================
        # LEFT SIDE
        # =====================================

        left_frame = tk.LabelFrame(
            main_frame,
            text="Arcade Status",
            padx=15,
            pady=15
        )

        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        self.status_label = tk.Label(
            left_frame,
            text="OFFLINE",
            font=(
                "Arial",
                22,
                "bold"
            )
        )

        self.status_label.pack(
            pady=10
        )

        self.server_label = tk.Label(
            left_frame,
            text="Server: Disconnected",
            font=(
                "Arial",
                14
            )
        )

        self.server_label.pack(
            pady=5
        )

        self.ip_label = tk.Label(
            left_frame,
            text=(
                "Arcade IP: "
                + self.network.get_local_ip()
            ),
            font=(
                "Arial",
                12
            )
        )

        self.ip_label.pack(
            pady=5
        )

        self.temp_label = tk.Label(
            left_frame,
            text="Temperature: 42°C",
            font=(
                "Arial",
                12
            )
        )

        self.temp_label.pack(
            pady=5
        )

        self.cpu_label = tk.Label(
            left_frame,
            text="CPU: 20%",
            font=(
                "Arial",
                12
            )
        )

        self.cpu_label.pack(
            pady=5
        )

        self.latency_label = tk.Label(
            left_frame,
            text="Latency: -- ms",
            font=(
                "Arial",
                12
            )
        )

        self.latency_label.pack(
            pady=5
        )

        self.heartbeat_label = tk.Label(
            left_frame,
            text="Heartbeats sent: 0",
            font=(
                "Arial",
                12
            )
        )

        self.heartbeat_label.pack(
            pady=5
        )

        ttk.Separator(
            left_frame
        ).pack(
            fill="x",
            pady=15
        )

        self.game_label = tk.Label(
            left_frame,
            text="Game: None",
            font=(
                "Arial",
                15,
                "bold"
            )
        )

        self.game_label.pack(
            pady=5
        )

        self.players_label = tk.Label(
            left_frame,
            text="Players: 0",
            font=(
                "Arial",
                13
            )
        )

        self.players_label.pack(
            pady=5
        )

        # =====================================
        # RIGHT SIDE
        # =====================================

        right_frame = tk.LabelFrame(
            main_frame,
            text="Simulator Controls",
            padx=15,
            pady=15
        )

        right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        tk.Button(
            right_frame,
            text="POWER ON",
            width=25,
            height=2,
            command=self.power_on
        ).pack(
            pady=5
        )

        tk.Button(
            right_frame,
            text="POWER OFF",
            width=25,
            height=2,
            command=self.power_off
        ).pack(
            pady=5
        )

        tk.Button(
            right_frame,
            text="CONNECT TO SERVER",
            width=25,
            height=2,
            command=self.connect_server
        ).pack(
            pady=5
        )

        tk.Button(
            right_frame,
            text="SEND HEARTBEAT",
            width=25,
            height=2,
            command=self.send_heartbeat
        ).pack(
            pady=5
        )

        ttk.Separator(
            right_frame
        ).pack(
            fill="x",
            pady=10
        )

        tk.Label(
            right_frame,
            text="Select Game"
        ).pack()

        self.game_select = ttk.Combobox(
            right_frame,
            values=[
                "Snake",
                "Pong",
                "Space Shooter",
                "Racing",
                "Battle Royale"
            ],
            state="readonly"
        )

        self.game_select.set(
            "Snake"
        )

        self.game_select.pack(
            pady=5
        )

        tk.Button(
            right_frame,
            text="START GAME",
            width=25,
            height=2,
            command=self.start_game
        ).pack(
            pady=5
        )

        tk.Button(
            right_frame,
            text="STOP GAME",
            width=25,
            height=2,
            command=self.stop_game
        ).pack(
            pady=5
        )

        
        ttk.Separator(
            right_frame
        ).pack(
            fill="x",
            pady=10
        )

        tk.Button(
            right_frame,
            text="PLAYER JOIN",
            width=25,
            command=self.player_join
        ).pack(
            pady=4
        )

        tk.Button(
            right_frame,
            text="PLAYER LEAVE",
            width=25,
            command=self.player_leave
        ).pack(
            pady=4
        )

        tk.Button(
            right_frame,
            text="SIMULATE ERROR",
            width=25,
            command=self.simuliraj_error
        ).pack(
            pady=4
        )

        tk.Label(
            right_frame,
            text="Oznaci error, ki ga hoces simulirat"
        ).pack()

        self.error_select = ttk.Combobox(
            right_frame,
            values=[
                "Network",
                "Controller",
                "Temperature",
                "Game",
                "Server",
                "Database",
                "Display"
            ],
            state="readonly"
        )

        self.error_select.set(
            "Network"
        )

        self.error_select.pack(
            pady=5
        )

        ######################################## Naprej je log

        log_frame = tk.LabelFrame(
            self.root,
            text="System Log"
        )

        log_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.log = tk.Text(
            log_frame,
            height=10,
            state="disabled"
        )

        self.log.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.write_log(
            "Simulator initialized."
        )


    ################################# Errorji simuliranje


    def simuliraj_error(self):
        error = self.error_select.get()

        print("Izbran error:", error)

        if error == "Network":
            self.ip = None
            self.server_connected = False
            print("Simuliram Network error")

        elif error == "Controller":
            print("Simuliram Controller error")

        elif error == "Temperature":
            self.temperature = 100
            self.artificial_cpu_usage = 100
            self.power_off()
            print("Simuliram Temperature error")

        elif error == "Game":
            print("Simuliram Game error")

        elif error == "Server":
            self.server_connected = False
            
            print("Simuliram Server error")

        elif error == "Database":
            print("Simuliram Database error")

        elif error == "Display":
            print("Simuliram Display error")

        



    # =============================================
    # LOG
    # =============================================

    def write_log(
        self,
        message
    ):

        timestamp = time.strftime(
            "%H:%M:%S"
        )

        self.log.config(
            state="normal"
        )

        self.log.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )

        self.log.see(
            "end"
        )

        self.log.config(
            state="disabled"
        )

    # =============================================
    # SERVER SYNC
    # =============================================

    def sync_server_state(self):

        if not self.server_connected:
            return False
    
        start_time = time.time()
    
        success = self.network.send_heartbeat(
            temperature=self.temperature,
            cpu_usage=self.cpu_usage,
            players=self.players,
            game=self.current_game
        )
    
        end_time = time.time()
    
        self.latency = int(
            (end_time - start_time) * 1000
        )
    
        if success:
        
            self.heartbeat_count += 1
    
            self.write_log(
                "State synchronized with server."
            )
    
        else:
        
            self.write_log(
                "WARNING: Server synchronization failed."
            )
    
        self.update_labels()
    
        return success
    # =============================================
    # POWER
    # =============================================

    def power_on(self):

        if self.arcade_online:

            self.write_log(
                "Arcade is already powered on."
            )

            return
        elif (self.temperature > 80) or (self.cpu_usage > 90):

            self.write_log(
                "ERROR: Cannot power on due to high temperature or CPU usage."
            )

            return
        else:
            self.arcade_online = True

            self.status_label.config(
                text="ONLINE"
            )

            self.write_log(
                "Arcade powered ON."
            )

    def power_off(self):

        # Pred izklopom serverju pošljemo zadnje stanje

        if self.server_connected:

            self.players = 0
            self.current_game = None

            self.sync_server_state()

        self.arcade_online = False

        self.server_connected = False

        self.players = 0

        self.current_game = None

        self.status_label.config(
            text="OFFLINE"
        )

        self.server_label.config(
            text="Server: Disconnected"
        )

        self.update_labels()

        self.write_log(
            "Arcade powered OFF."
        )

    # =============================================
    # SERVER CONNECTION
    # =============================================

    def connect_server(self):

        if not self.arcade_online:

            self.write_log(
                "ERROR: Arcade must be powered on first."
            )

            return

        self.write_log(
            "Checking connection to server..."
        )

        if not self.network.check_server():

            self.server_connected = False

            self.server_label.config(
                text="Server: Disconnected"
            )

            self.write_log(
                "ERROR: Server unavailable."
            )

            return

        self.server_connected = True

        self.server_label.config(
            text="Server: Connected"
        )

        self.write_log(
            "Connected to server."
        )

        # Registracija

        if self.network.register_arcade():

            self.write_log(
                "Arcade registered."
            )

        else:

            self.write_log(
                "WARNING: Registration failed."
            )

        # takoj po registraciji pošljemo stanje

        self.sync_server_state()

    # =============================================
    # HEARTBEAT
    # =============================================

    def send_heartbeat(self):

        if not self.server_connected:

            self.write_log(
                "ERROR: Server disconnected."
            )

            return

        self.sync_server_state()

    # =============================================
    # GAME
    # =============================================

    def start_game(self):

        if not self.arcade_online:

            self.write_log(
                "ERROR: Arcade is offline."
            )

            return

        self.current_game = (
            self.game_select.get()
        )

        self.write_log(
            f"Game started: {self.current_game}"
        )

        self.update_labels()

        # POŠLJI SERVERJU

        self.sync_server_state()

    def stop_game(self):

        if self.current_game is None:

            self.write_log(
                "No game is currently running."
            )

            return

        self.write_log(
            f"Game stopped: {self.current_game}"
        )

        self.current_game = None

        self.update_labels()

        # POŠLJI SERVERJU

        self.sync_server_state()

    # =============================================
    # PLAYERS
    # =============================================

    def player_join(self):

        if not self.arcade_online:

            self.write_log(
                "ERROR: Arcade is offline."
            )

            return

        self.players += 1

        self.write_log(
            f"Player joined. Players: {self.players}"
        )

        self.update_labels()

        # POŠLJI SERVERJU

        self.sync_server_state()

    def player_leave(self):

        if self.players <= 0:

            self.write_log(
                "No players connected."
            )

            return

        self.players -= 1

        self.write_log(
            f"Player left. Players: {self.players}"
        )

        self.update_labels()

        # POŠLJI SERVERJU

        self.sync_server_state()


    # =============================================
    # LABELS
    # =============================================

    def update_labels(self):

        game_text = (
            self.current_game
            if self.current_game
            else "None"
        )

        self.game_label.config(
            text=f"Game: {game_text}"
        )

        self.players_label.config(
            text=f"Players: {self.players}"
        )

        self.temp_label.config(
            text=(
                f"Temperature: "
                f"{self.temperature:.1f}°C"
            )
        )

        self.cpu_label.config(
            text=(
                f"CPU: "
                f"{self.cpu_usage}%"
            )
        )

        if self.server_connected:

            self.latency_label.config(
                text=f"Latency: {self.latency} ms"
            )

        else:

            self.latency_label.config(
                text="Latency: -- ms"
            )

        self.heartbeat_label.config(
            text=(
                f"Heartbeats sent: "
                f"{self.heartbeat_count}"
            )
        )

    def update_system(self):

        if self.arcade_online:

            self.temperature += (
                random.uniform(
                    -0.4,
                    0.8
                )
            )

            self.temperature = max(
                35,
                min(
                    self.temperature,
                    85
                )
            )

            self.cpu_usage = random.randint(
                10,
                90
            )

        else:

            self.temperature += (
                30
                -
                self.temperature
            ) * 0.05

            self.cpu_usage = 0

        self.update_labels()

        self.root.after(
            1000,
            self.update_system
        )


root = tk.Tk()

app = ArcadeSimulator(
    root
)

root.mainloop()