import config
import function
import sys


def main():
    pallet_id = function.random_id_pallet(6)
    try:
        for i in function.parser(sys.argv[1]):
            if i["Тип"] == "Задания на палеты в работе" and i["Полученные данные"]["action"] == "start_picking":
                start_data = i["Полученные данные"]
                start_data["pallets"][0]["pallet_id"] = pallet_id
                start_data["device_id"] = config.device_id

                function.requestPOST(config.url_start_picking, config.headers, start_data)

            elif i["Тип"] == "Факт отбора":
                input("\nНажмите любую клавишу")
                selection = i["Полученные данные"]
                selection["pallet_id"] = pallet_id
                selection["device_id"] = config.device_id

                function.requestPOST(config.url_fact_command, config.headers, selection)

                print(f"cell: {selection['product']['cell']}")

            elif i["Тип"] == "Измененное задание":
                print("\nИзмененное задание")
                change_route = i["Полученные данные"]
                change_route["pallets"][0]["pallet_id"] = pallet_id
                change_route["device_id"] = config.device_id
                print(f"pallet_id: ", change_route["pallets"][0]["order_id"])

                function.requestPOST(config.url_change_route, config.headers, change_route)

            else:
                print("Конец файла")

    except Exception:
        print("Что то пошло не так")


if __name__ == "__main__":
    main()
