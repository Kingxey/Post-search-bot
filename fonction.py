
channel_group_map = {}
users = set()

def connect_channel_to_group(channel_id: str, group_id: int) -> str:
    channel_group_map[channel_id] = group_id
    return f"✅ Le canal {channel_id} a été connecté au groupe {group_id}."

def list_connected_channels() -> str:
    if not channel_group_map:
        return "📭 Aucun canal connecté."
    
    text = "📡 Canaux connectés :\n\n"
    for chan, grp in channel_group_map.items():
        text += f"🔸 Canal: `{chan}` → Groupe: `{grp}`\n"
    return text

def disconnect_channel(channel_id: str) -> str:
    if channel_id in channel_group_map:
        del channel_group_map[channel_id]
        return f"🔌 Canal {channel_id} déconnecté avec succès."
    return "⚠️ Ce canal n'est pas connecté."

def register_user(user_id: int):
    users.add(user_id)

def get_total_users() -> int:
    return len(users)

def get_total_channels() -> int:
    return len(channel_group_map)

def get_stats() -> str:
    return (
        f"📊 Statistiques :\n"
        f"👤 Utilisateurs : {get_total_users()}\n"
        f"📡 Canaux connectés : {get_total_channels()}"
    )

def get_all_users() -> set:
    return users
