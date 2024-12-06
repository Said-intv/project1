class Activity:
    def __init__(self, name, day, time):
        self.name = name
        self.day = day
        self.time = time

    def __str__(self):
        return f"{self.time} - {self.name}"


class Calender:
    def __init__(self):
        self.schedule = {
            "Senin": [],
            "Selasa": [],
            "Rabu": [],
            "Kamis": [],
            "Jumat": [],
            "Sabtu": [],
            "Minggu": []
        }

    # Create: Tambah aktivitas
    def add_activity(self, name, day, time):
        if day in self.schedule:
            activity = Activity(name, day, time)
            self.schedule[day].append(activity)
            print(f"Activity '{name}' added to {day} at {time}.")
        else:
            print(f"Invalid day: {day}. Please enter a valid day of the week.")

    # Read: Lihat aktivitas
    def view_schedule(self):
        for day, activities in self.schedule.items():
            print(f"\n{day}:")
            if activities:
                for index, activity in enumerate(activities):
                    print(f"  {index + 1}. {activity}")
            else:
                print("  No activities scheduled.")

    # Update: Perbarui aktivitas
    def update_activity(self, day, index, new_name=None, new_time=None):
        if day in self.schedule and 0 <= index < len(self.schedule[day]):
            activity = self.schedule[day][index]
            if new_name:
                activity.name = new_name
            if new_time:
                activity.time = new_time
            print(f"Activity updated successfully on {day}.")
        else:
            print(f"Invalid day or activity index.")

    # Delete: Hapus aktivitas
    def delete_activity(self, day, index):
        if day in self.schedule and 0 <= index < len(self.schedule[day]):
            removed_activity = self.schedule[day].pop(index)
            print(f"Activity '{removed_activity.name}' removed from {day}.")
        else:
            print(f"Invalid day or activity index.")


def main():
    system = Calender()
    while True:
        print("\n=== Calendar Activity System ===")
        print("1. Tambah Aktivitas")
        print("2. Lihat Jadwal")
        print("3. Perbarui Aktivitas")
        print("4. Hapus Aktivitas")
        print("5. Keluar")
        choice = input("Pilih opsi (1-5): ")

        if choice == '1':  # Create
            name = input("Masukkan nama aktivitas: ")
            day = input("Masukkan hari (Senin-Minggu): ")
            time = input("Masukkan waktu (misalnya 10:00 AM): ")
            system.add_activity(name, day, time)
        elif choice == '2':  # Read
            print("\nJadwal Mingguan:")
            system.view_schedule()
        elif choice == '3':  # Update
            day = input("Masukkan hari (Senin-Minggu): ")
            index = int(input("Masukkan nomor aktivitas yang ingin diperbarui (mulai dari 1): ")) - 1
            new_name = input("Masukkan nama baru (kosongkan jika tidak ingin diubah): ")
            new_time = input("Masukkan waktu baru (kosongkan jika tidak ingin diubah): ")
            system.update_activity(day, index, new_name if new_name else None, new_time if new_time else None)
        elif choice == '4':  # Delete
            day = input("Masukkan hari (Senin-Minggu): ")
            index = int(input("Masukkan nomor aktivitas yang ingin dihapus (mulai dari 1): ")) - 1
            system.delete_activity(day, index)
        elif choice == '5':  # Exit
            print("Keluar dari sistem.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()