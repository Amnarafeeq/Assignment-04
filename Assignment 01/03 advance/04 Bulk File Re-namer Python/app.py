import os

def main():
    i = 0
    path = "c:/Users/Mubasher Computer/Downloads/"
    for filename in os.listdir(path):
        my_dest_name = "image" + str(i) + ".jpg"
        my_source = os.path.join(path, filename)
        my_dest = os.path.join(path, my_dest_name)

        try:
            os.rename(my_source, my_dest)
            print(f"Renamed: {filename} ➡ {my_dest_name}")
            i += 1
        except Exception as e:
            print(f"❌ Error renaming {filename}: {e}")

if __name__ == "__main__":
    main()
