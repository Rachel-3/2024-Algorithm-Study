def solution(friends, gifts):
    gifts_exchange = {f: {t: 0 for t in friends if t != f} for f in friends}

    for gift in gifts:
        giver, receiver = gift.split()
        gifts_exchange[giver][receiver] += 1

    gift_index = {f: 0 for f in friends}
    for giver in gifts_exchange:
        for receiver in gifts_exchange[giver]:
            gift_index[giver] += gifts_exchange[giver][receiver]
            gift_index[receiver] -= gifts_exchange[giver][receiver]

    next_month_gifts = {friend: 0 for friend in friends}
    processed_pairs = set()

    for f1 in friends:
        for f2 in friends:
            if f1 != f2 and (f2, f1) not in processed_pairs:
                g_to_r = gifts_exchange[f1].get(f2, 0)
                r_to_g = gifts_exchange[f2].get(f1, 0)

                if g_to_r > r_to_g:
                    next_month_gifts[f1] += 1
                elif g_to_r < r_to_g:
                    next_month_gifts[f2] += 1
                else:
                    if gift_index[f1] > gift_index[f2]:
                        next_month_gifts[f1] += 1
                    elif gift_index[f1] < gift_index[f2]:
                        next_month_gifts[f2] += 1
                    else:
                        pass

                processed_pairs.add((f1, f2))

    max_gifts = max(next_month_gifts.values())

    return max_gifts