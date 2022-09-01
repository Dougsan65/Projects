from operator import truediv
import pymem
import pymem.process
import keyboard
import time

dwEntityList = (0x4DDD91C)
dwLocalPlayer = (0xDC14CC)
m_iTeamNum = (0xF4)
dwGlowObjectManager = (0x53265D0)
m_iGlowIndex = (0x10488)
dwForceJump = (0x52878FC)
m_fFlags = (0x104)


pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll


def main():
    glowmodule()


def glowmodule():
    print('foi')
    while True:
        glow = pm.read_int(client + dwGlowObjectManager)
        for i in range(0, 32):
            entity = pm.read_int(client + dwEntityList + i *0x10)
            
            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entityglowing = pm.read_int(entity + m_iGlowIndex)
                    
                if entity_team_id == 2: #tr
                    

                    pm.write_float(glow + entityglowing * 0x38 + 0x8, float(1))   # R
                    pm.write_float(glow + entityglowing * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow + entityglowing * 0x38 + 0x10, float(0))  # B
                    pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)           # Enable glow

                elif entity_team_id == 3: #ct
                    
                    pm.write_float(glow + entityglowing * 0x38 + 0x8, float(0))   # R
                    pm.write_float(glow + entityglowing * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow + entityglowing * 0x38 + 0x10, float(1))  # B
                    pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)           # Enable glow

            if keyboard.is_pressed("space"):
                force_jump = client + dwForceJump
                player = pm.read_int(client + dwLocalPlayer)
                on_ground = pm.read_int(player + m_fFlags)
                if player and on_ground and on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    pm.write_int(force_jump, 4)



if __name__ == '__main__':
    main()