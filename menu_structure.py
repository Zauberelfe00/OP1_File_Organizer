WifiTransfer = [
    ["Wifi Transfer", -1],
    ["Start Server", "Open SSH"]
    # "Connect", -1
]


MIDI =[
    ["MIDI", -1],
    ["USB MIDI IN Test", "USB_MIDI_In_Test"],
    ["USB MIDI OUT Test", "USB_MIDI_Out_Test"]
]

Utilities = [
    ["Utilities", -1],
    ["Check Storage", "checkStorage"],
    ["Mount/Eject OP-1", "act_ESC_Mount_OP_1"],
    ["MIDI Host", MIDI],
    ["Power Off System", "act_POWER_OFF"],
]

# PresetPage = [
#     ["Manage Presets", -1],
#     ["Freeze State", "act_Freeze_State"],
#     ["Upload From Local", "act_Upload_Preset_From_Local"],
#     ["Del All User Data", "act_DANG_Delete_ALL_From_OP_1"]
# ]

OP_1_Patches_Folder = [
    ["OP-1 Patches", -1],
    ["Synth", "OP-1 Synth Patches"],  # Start Browser
    ["Drum", "OP-1 Drum Patches"]  # Start Browser
]

Local_Patches = [
    ["Local Patches", -1],
    ["Synth", "UploadSynthPatches"],  # Start Browser
    ["Drum", "UploadDrumPatches"]  # Start Browser
]

OP_1_Patches = [
    ["OP-1", -1],
    ["Synth", "OP1_Synth_Patches"],  # Start Browser
    ["Drum", "OP1_Drum_Patches"]  # Start Browser
]

PatchesPage = [
    ["Manage Patches", -1],
    ["Backup Patches", "act_5_Backup_All_Patches"],
    ["Local Patches", Local_Patches],
    ["Manage OP-1 Patches", OP_1_Patches]
]

BackupPage =[
    ["Backup Projects", -1],
    ["Backup tracks + album", "act_Backup_Project_From_OP_1"],
    ["Backup tracks", "act_Load_Project_From_Local_only_tracks"]
]

ProjectsPage = [
    ["Manage Projects", -1],
    ["Backup Project", BackupPage],
    ["Local Projects", "act_Load_Project_From_Local"]
]


OP1 = [
    ["OP-1", -1],
    ["Projects", ProjectsPage],
    ["Patches", PatchesPage]
]

OPZ = [
    ["OP-Z", -1]
]

MainPage = [
    ["Main Menu", -1],
    ["OP-1", OP1],
    ["OP-Z", OPZ],
    ["Wifi Transfer", WifiTransfer],
    ["Utilities", Utilities],
]

