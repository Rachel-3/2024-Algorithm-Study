def solution(bandage, health, attacks):
    t, x, y = bandage
    current_health = health
    success_recovery = 0
    current_time = 0

    for attack_time, damage in attacks:
        while current_time < attack_time:
            success_recovery += 1
            if success_recovery < t:
                current_health += x
            elif success_recovery == t:
                current_health += x + y
                success_recovery = 0
            
            current_health = min(current_health, health)
            
            current_time += 1
        
        current_health -= damage
        if current_health <= 0:
            return -1
        
        success_recovery = 0
        current_time = attack_time
        current_time += 1

    return current_health