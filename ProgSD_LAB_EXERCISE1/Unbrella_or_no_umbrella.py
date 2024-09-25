def main():
    rain_status = input("Is it raining(Yes/No): ")
    rain_status = rain_status.lower()

    if rain_status == 'yes':
        wind_status = input("Is it winding(Yes/No): ")
        wind_status = wind_status.lower()

        if wind_status == 'yes':
            print("It's too windy for an umbrella.")
        else:
            print("Take an umbrella.")
    else:
        print("Enjoy your day.")

if __name__ == '__main__':
    main()