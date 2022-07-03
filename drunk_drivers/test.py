def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

avg_score = "7.88"
avg_score = round(float(avg_score), 1)
if avg_score <= 5.9:
    avg_score_colored = colored(225, 0, 0, str(avg_score))
    avg_score_colored = avg_score_colored.replace(" ", "")
elif avg_score >= 6 and avg_score <= 7.9:
    avg_score_colored = colored(255, 191, 0, str(avg_score))
    avg_score_colored = avg_score_colored.replace(" ", "")
elif avg_score >= 8:
    avg_score_colored = colored(0, 132, 80, str(avg_score))
    avg_score_colored = avg_score_colored.replace(" ", "")

print("Driver\'s rating: " + avg_score_colored +"/10")