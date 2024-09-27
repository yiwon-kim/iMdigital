class Spaceship:
    def __init__(self, color: str, speed: int, passengers: int):
        self._color = color
        self._speed = speed
        self._passengers = passengers

    # Color getter and setter
    def get_color(self) -> str:
        return self._color

    def set_color(self, color: str):
        self._color = color

    # Speed getter and setter
    def get_speed(self) -> int:
        return self._speed

    def set_speed(self, speed: int):
        self._speed = speed

    # Passengers getter and setter
    def get_passengers(self) -> int:
        return self._passengers

    def set_passengers(self, passengers: int):
        self._passengers = passengers

    def add_passenger(self, number: int):
        self._passengers += number
        print(f"{number}명의 탑승자가 추가되었습니다. 현재 탑승인원: {self._passengers}")

    def remove_passenger(self, number: int):
        if self._passengers >= number:
            self._passengers -= number
            print(f"{number}명의 탑승자가 하차했습니다. 현재 탑승인원: {self._passengers}")
        else:
            print("하차할 탑승객 수가 현재 탑승인원보다 많습니다")

    def increase_speed(self, amount: int):
        self._speed += amount
        print(f"속도가 {amount}만큼 증가했습니다. 새로운 속도: {self._speed}")

    def decrease_speed(self, amount: int):
        if self._speed - amount >= 0:
            self._speed -= amount
            print(f"속도가 {amount}만큼 감소했습니다. 새로운 속도: {self._speed}")
        else:
            print("속도는 음수가 될 수 없습니다")

    def get_info(self) -> str:
        return f"우주선 색상: {self._color}, 속도: {self._speed}, 탑승인원: {self._passengers}"

def simulate_spaceship():
    spaceship = Spaceship("Red", 10000, 5)
    
    while True:
        print("\n현재 우주선 상태:")
        print(spaceship.get_info())
        
        print("\n무엇을 하시겠습니까?")
        print("1. 색상 설정")
        print("2. 속도 증가")
        print("3. 속도 감소")
        print("4. 탑승인원 추가")
        print("5. 탑승인원 하차")
        print("6. 시뮬레이션 종료")
        
        choice = input("선택을 입력하세요 (1-6): ")

        if choice == '1':
            color = input("새 색상을 입력하세요: ")
            spaceship.set_color(color)
            print(f"색상이 {color}(으)로 변경되었습니다")
        
        elif choice == '2':
            amount = int(input("속도를 얼마나 증가시키겠습니까?: "))
            spaceship.increase_speed(amount)
        
        elif choice == '3':
            amount = int(input("속도를 얼마나 감소시키겠습니까?: "))
            spaceship.decrease_speed(amount)
        
        elif choice == '4':
            number = int(input("추가할 탑승인원 수를 입력하세요: "))
            spaceship.add_passenger(number)
        
        elif choice == '5':
            number = int(input("하차할 탑승인원 수를 입력하세요: "))
            spaceship.remove_passenger(number)
        
        elif choice == '6':
            print("시뮬레이션을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다. 1에서 6 사이의 숫자를 입력하세요.")

simulate_spaceship()