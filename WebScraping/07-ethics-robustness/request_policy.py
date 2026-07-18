from urllib.robotparser import RobotFileParser

def allowed(robots_url: str, target_url: str, user_agent: str = "LearningScraper") -> bool:
    parser = RobotFileParser()
    parser.set_url(robots_url)
    parser.read()
    return parser.can_fetch(user_agent, target_url)

if __name__ == "__main__":
    print("Önce robots.txt iznini kontrol edin; izin yoksa istek göndermeyin.")
