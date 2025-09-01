# Base class for Superhero
class Superhero:
    def __init__(self, name, power_level, city):
        self._name = name  # Encapsulation with protected attribute
        self._power_level = power_level
        self._city = city
        self._is_active = True

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for power_level with validation
    @property
    def power_level(self):
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        if value < 0:
            raise ValueError("Power level cannot be negative")
        self._power_level = value

    # Method to toggle active status
    def toggle_active(self):
        self._is_active = not self._is_active
        return f"{self._name} is now {'active' if self._is_active else 'inactive'}"

    # Abstract-like method for polymorphism (to be overridden)
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

    # Common method for all superheroes
    def protect_city(self):
        if self._is_active:
            return f"{self._name} is protecting {self._city} with power level {self._power_level}!"
        return f"{self._name} is currently inactive."

# Derived class for a flying superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power_level, city, flight_speed):
        super().__init__(name, power_level, city)
        self.flight_speed = flight_speed

    def move(self):
        return f"{self._name} is flying at {self.flight_speed} mph!"

    def special_ability(self):
        return f"{self._name} soars above {self._city} with incredible speed!"

# Derived class for a running superhero
class RunningSuperhero(Superhero):
    def __init__(self, name, power_level, city, run_speed):
        super().__init__(name, power_level, city)
        self.run_speed = run_speed

    def move(self):
        return f"{self._name} is running at {self.run_speed} mph!"

    def special_ability(self):
        return f"{self._name} dashes through {self._city} with super speed!"

# Example usage
def main():
    # Create instances of different superheroes
    sky_striker = FlyingSuperhero("Sky Striker", 85, "Metropolis", 500)
    flash_runner = RunningSuperhero("Flash Runner", 90, "Gotham", 200)

    # Demonstrate polymorphism with move()
    heroes = [sky_striker, flash_runner]
    for hero in heroes:
        print(hero.move())
        print(hero.protect_city())
        print(hero.special_ability())
        print(hero.toggle_active())
        print()

if __name__ == "__main__":
    main()
    