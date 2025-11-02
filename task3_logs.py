import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return None
    
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }


def load_logs(file_path: str) -> list:
    logs = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parsed_log = parse_log_line(line)
                    if parsed_log:
                        logs.append(parsed_log)
        return logs
    
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    
    return counts


def display_log_counts(counts: dict):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python task3_logs.py <шлях_до_лог_файлу> [рівень_логування]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None
    
    logs = load_logs(file_path)
    
    if not logs:
        print("Не вдалося завантажити логи.")
        return
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if log_level:
        print(f"\nДеталі логів для рівня '{log_level}':")
        filtered_logs = filter_logs_by_level(logs, log_level)
        
        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Записів з рівнем '{log_level}' не знайдено.")


if __name__ == "__main__":
    main()
