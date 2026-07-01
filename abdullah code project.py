class ElectricVehicle:
    """Represents an Electric Vehicle."""
    def __init__(self, model: str, battery_level: int):
        self.model = model
        self.battery_level = battery_level  # Percentage (0-100)

    def charge(self):
        """Simulates charging the vehicle to 100%."""
        self.battery_level = 100
        print(f"⚡ {self.model} has been fully charged to {self.battery_level}%!")


class ChargingSlot:
    """Represents an individual charging spot in the station."""
    def __init__(self, slot_id: int, slot_type: str):
        self.slot_id = slot_id
        self.slot_type = slot_type  # e.g., "Fast" or "Standard"
        self.is_occupied = False
        self.current_vehicle = None

    def assign_vehicle(self, vehicle: ElectricVehicle):
        """Occupies the slot with a vehicle."""
        self.is_occupied = True
        self.current_vehicle = vehicle
        print(f" Slot {self.slot_id} ({self.slot_type}) assigned to {vehicle.model}.")

    def release_slot(self):
        """Frees up the slot after charging is done."""
        print(f" Slot {self.slot_id} is now vacant.")
        self.is_occupied = False
        self.current_vehicle = None


class ChargingStation:
    """Manages the entire charging station and its slots."""
    def __init__(self, name: str):
        self.name = name
        self.slots = []

    def add_slot(self, slot: ChargingSlot):
        """Adds a new charging spot to the station."""
        self.slots.append(slot)

    def display_status(self):
        """Prints the current state of all slots."""
        print(f"\n--- {self.name} Current Status ---")
        for slot in self.slots:
            status = f"Occupied by {slot.current_vehicle.model}" if slot.is_occupied else "Available"
            print(f"Slot {slot.slot_id} [{slot.slot_type}]: {status}")
        print("-" * 35)

    def process_charging(self, vehicle: ElectricVehicle):
        """Finds an available slot, charges the vehicle, and releases the slot."""
        for slot in self.slots:
            if not slot.is_occupied:
                print(f"\n[Incoming] {vehicle.model} (Current Battery: {vehicle.battery_level}%) requested charging.")
                slot.assign_vehicle(vehicle)
                self.display_status()
                
                # Simulate charging action
                vehicle.charge()
                slot.release_slot()
                return
        
        print(f"\n❌ Sorry, no slots available for {vehicle.model} right now.")


# --- Interactive Presentation Demonstration ---
if __name__ == "__main__":
    # 1. Initialize the Station and standard slots
    hub = ChargingStation("EcoCharge Hub")
    hub.add_slot(ChargingSlot(1, "Fast"))
    hub.add_slot(ChargingSlot(2, "Standard"))

    print("=== EV Charging Station Management System ===")
    hub.display_status()

    # 2. Loop to demand continuous user input for presentation interaction
    while True:
        print("\n--- Register a New Vehicle ---")
        model_input = input("Enter EV Model (or type 'exit' to quit): ").strip()
        
        if model_input.lower() == 'exit':
            print("Exiting presentation mode. Thank you!")
            break
            
        if not model_input:
            print("Model name cannot be empty. Try again.")
            continue

        # Exception handling to make sure battery level input is a proper number
        try:
            battery_input = int(input("Enter current battery percentage (0-100): "))
            if not (0 <= battery_input <= 100):
                print("⚠️ Battery percentage must be between 0 and 100!")
                continue
        except ValueError:
            print("⚠️ Invalid input! Please enter a whole number for battery percentage.")
            continue

        # 3. Create the Object from User Input and process it
        user_vehicle = ElectricVehicle(model_input, battery_input)
        hub.process_charging(user_vehicle)
        
        # Show final station status after processing
        hub.display_status()