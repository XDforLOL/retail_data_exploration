from typing import NoReturn
import os
import random
import psycopg2
import string


conn = psycopg2.connect(dbname="postgres",
                        user="postgres",
                        password=os.environ.get('psql_pass'),
                        host=os.environ.get('psql_ip'))
cursor = conn.cursor()


def insert_product(product_id, product_name, model, maker, stock, price) -> NoReturn:
    cursor.execute(f"INSERT INTO ksp.products VALUES ({product_id},"
                   f"'{product_name}','{model}','{maker}' ,'{stock}', '{price}')")
    conn.commit()


def get_model() -> str:
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(6)))
    sample_str += ''.join((random.choice(string.digits) for i in range(3)))
    model_list = list(sample_str)
    random.shuffle(model_list)
    model = ''.join(model_list)
    return model


def get_valid_product_id() -> str:
    cursor.execute('select MAX(product_id) from ksp.products')
    highest_id = cursor.fetchall()
    return highest_id[0][0] + 1


def get_valid_product() -> dict:
    makers = ['Asus', 'HTC', 'Huawei', 'LG Electronics', 'Meizu', 'Motorola Mobility', 'Xiaomi', 'OnePlus']
    model = get_model()
    maker = random.choice(makers)
    product_name = f"{maker} {model}"
    product_names = (
        ' Asus ZenFone 5 : Asus', ' ZenFone 4 : Asus', ' Asus ZenFone 6 : Asus', ' Asus ZenFone 4.5 : Asus',
        ' Asus ZenFone 5 : Asus', ' Asus ZenFone 5 : Asus', ' Asus ZenFone 2 : Asus', ' Asus ZenFone 3 : Asus',
        ' Asus ZenFone 4 : Asus', ' Asus ZenFone Max M1 : Asus', ' Asus ZenFone Max Pro M1 : Asus',
        ' Asus ZenFone 5 : Asus', ' Asus ROG Phone : Asus', ' Asus ZenFone Max M2 : Asus',
        ' Asus ZenFone Max Pro M2 : Asus', ' Asus ZenFone 6  : Asus', ' Asus ROG Phone II : Asus',
        ' Asus ROG : Asus', ' Phone 3 : Asus', ' Asus ZenFone 7 : Asus', ' BlackBerry Priv BlackBerry Mobile',
        ' BlackBerry DTEK50 Limited : BlackBerry Mobile', ' BlackBerry DTEK60 : BlackBerry Mobile',
        ' BlackBerry Limited : BlackBerry Mobile', ' BlackBerry Aurora : BlackBerry Mobile',
        ' BlackBerry KeyOne : BlackBerry Mobile 7.0', ' BlackBerry Motion : BlackBerry Mobile',
        ' BlackBerry Key2 : BlackBerry Mobile', ' Key2 LE : BlackBerry Mobile', ' HTC Hero : HTC',
        ' HTC Tattoo : HTC', ' HTC Desire : HTC', ' HTC Legend : HTC', ' HTC Droid Incredible : HTC',
        ' HTC Wildfire : HTC', ' HTC Aria : HTC', ' HTC Evo 4G : HTC', ' HTC Desire HD : HTC',
        ' HTC Desire Z  : HTC', ' HTC Evo Shift 4G : HTC', ' HTC Inspire 4G : HTC', ' HTC Incredible S : HTC',
        ' HTC ThunderBolt : HTC', ' HTC Desire S : HTC', ' HTC Sensation : HTC', ' Wildfire S : HTC',
        ' HTC ChaCha : HTC', ' HTC Salsa : HTC', ' HTC Evo 3D : HTC', ' HTC Amaze 4G : HTC', ' Explorer : HTC',
        ' HTC Raider 4G : HTC', ' HTC Evo Design 4G : HTC', ' Rezound : HTC', ' HTC One S : HTC',
        ' HTC One V : HTC', ' HTC One X : HTC', ' HTC Evo 4G LTE : HTC', ' HTC Droid Incredible 4G LTE : HTC',
        ' HTC Desire X : HTC', ' Butterfly : HTC', ' HTC One : HTC', ' HTC One Mini : HTC',
        ' HTC One Max HTC 4.1', ' HTC One  : HTC', ' HTC One Mini 2 : HTC', ' HTC Desire Eye : HTC',
        ' HTC Desire : HTC', ' 620 : HTC', ' HTC One M9 : HTC', ' HTC 10  : HTC', ' HTC U Ultra : HTC',
        ' HTC U11 : HTC', ' HTC U11+ 11 Life : HTC', ' Honor 6 : Huawei', ' Honor 4X : Huawei',
        ' Honor 7 : Huawei', ' Honor 5X : Huawei', ' Honor 8 : Huawei', ' Honor 8 Pro : Huawei',
        ' Honor 9 : Huawei', ' Honor 8X : Huawei', ' Huawei Honor 20 : Huawei', ' Huawei 10 : Huawei',
        ' Honor 30 : Huawei', ' Huawei Ascend P1 : Huawei', ' Huawei Ascend Mate : Huawei',
        ' Huawei Ascend P2 : Huawei', ' Huawei Ascend P6 : Huawei', ' Huawei Ascend Mate 2 4G',
        ' Huawei Ascend P7 : Huawei', ' Huawei Ascend Mate 7 : Huawei', ' Huawei P8 : Huawei',
        ' Mate S : Huawei', ' Huawei Mate 8 : Huawei', ' Huawei P9 : Huawei', ' Huawei Mate 9 : Huawei',
        ' Huawei P10 : Huawei', ' Huawei Mate 10 : Huawei', ' Huawei P20 : Huawei', ' Huawei Mate 20 : Huawei',
        ' Huawei P30 : Huawei', ' Huawei Mate 30 : Huawei', ' Huawei P40 : Huawei',
        ' Lenovo Legion Pro/Duel Lenovo', ' LG GW620 LG  : LG Electronics', ' LG Optimus Q : LG Electronics',
        ' LG Optimus : LG Electronics', ' LG Optimus One : LG Electronics', ' LG Optimus Chic : LG Electronics',
        ' LG Optimus 2X : LG Electronics', ' LG Optimus Black : LG Electronics',
        ' LG Optimus 3D : LG Electronics', ' LG Optimus Slider : LG Electronics',
        ' LG Optimus LTE : LG Electronics', ' LG Optimus 4X HD : LG Electronics',
        ' LG Optimus L9 : LG Electronics', ' LG Optimus Vu : LG Electronics', ' LG Optimus G LG Electronics',
        ' LG G2 : LG Electronics', ' LG G Flex : LG Electronics', ' LG G Pro Lite : LG Electronics',
        ' LG Gx : LG Electronics', ' LG G2 Mini : LG Electronics', ' LG G Pro 2 : LG Electronics',
        ' LG G3 : LG Electronics', ' LG G3 Stylus : LG Electronics', ' LG G Flex 2 : LG Electronics',
        ' LG G4 : LG Electronics', ' V10 : LG Electronics', ' LG K10 : LG Electronics',
        ' LG G5 : LG Electronics', ' LG V20 : LG Electronics', ' LG K10 : LG Electronics',
        ' LG G6 : LG Electronics', ' LG V30 : LG Electronics', ' LG G7 ThinQ : LG Electronics',
        ' V35 ThinQ : LG Electronics', ' LG K10 : LG Electronics', ' LG V40 ThinQ : LG Electronics',
        ' LG G8 ThinQ  : LG Electronics', ' LG V50 ThinQ : LG Electronics', ' LG V60 ThinQ : LG Electronics',
        ' LG Velvet : LG Electronics', ' Meizu M9 : Meizu', ' Meizu MX : Meizu', ' Meizu MX 4-core : Meizu',
        ' Meizu MX2 : Meizu', ' Meizu MX3 : Meizu', ' Meizu MX4 : Meizu', ' Meizu MX4 Pro : Meizu',
        ' Meizu 1 Note : Meizu', ' Meizu M2 Note : Meizu', ' Meizu MX5 : Meizu', ' Meizu M2 : Meizu',
        ' Meizu PRO 5 : Meizu', ' Meizu M3 Note : Meizu', ' Meizu PRO 6 : Meizu', ' Meizu M3s : Meizu',
        ' Meizu MX6 : Meizu', ' Meizu M3E : Meizu', ' Meizu U10 20 : Meizu', ' Meizu M3 Max : Meizu',
        ' Meizu M5 : Meizu', ' Meizu PRO 6 Plus : Meizu', ' Meizu M5 Note : Meizu', ' Meizu M6 Note : Meizu',
        ' Motorola Cliq : Motorola', ' Motorola Droid : Motorola', ' Motorola Backflip : Motorola',
        ' Motorola Flipout : Motorola', ' Motorola Droid X : Motorola', ' Motorola Charm : Motorola',
        ' Motorola Droid 2 : Motorola', ' Motorola Defy : Motorola', ' Motorola Droid Pro : Motorola',
        ' Motorola Atrix 4G : Motorola Mobility', ' Motorola Droid 3 : Motorola Mobility',
        ' Motorola Droid Bionic : Motorola Mobility', ' Motorola Atrix 2 : Motorola Mobility',
        ' Motorola Droid Razr : Motorola Mobility', ' Motorola Droid 4 : Motorola Mobility',
        ' Motorola Photon Q : Motorola Mobility', ' Motorola Droid Razr M : Motorola Mobility',
        ' Motorola Droid Razr HD : Motorola Mobility', ' Motorola Droid Maxx : Motorola Mobility',
        ' Motorola Droid Mini : Motorola Mobility', ' Moto X Motorola Droid Turbo Motorola Mobility',
        ' Moto G : Motorola Mobility', ' Moto X Play : Motorola Mobility', ' Moto X Style : Motorola Mobility',
        ' Moto G4 : Motorola Mobility', ' Moto E3 : Motorola Mobility', ' Moto Z : Motorola Mobility',
        ' Moto Z Play : Motorola Mobility', ' Moto G5 : Motorola Mobility', ' Moto C : Motorola Mobility',
        ' Moto E4 : Motorola Mobility', ' Moto Z2 Play : Motorola Mobility', ' Moto X4 : Motorola Mobility',
        ' Moto E5 : Motorola Mobility', ' Moto G6 : Motorola Mobility', ' Moto Z3 Play : Motorola Mobility',
        ' Motorola One : Motorola Mobility', ' Moto G7 : Motorola Mobility',
        ' Motorola One : Motorola Mobility', ' Moto Z4 : Motorola Mobility',
        ' Motorola One : Motorola Mobility', ' Moto G8 Plus : Motorola Mobility',
        ' Motorola One : Motorola Mobility', ' Motorola One : Motorola Mobility',
        ' Motorola Razr : Motorola Mobility', ' Motorola One : Motorola Mobility',
        ' Moto G8 Power : Motorola Mobility', ' Moto G Power/Stylus : Motorola Mobility',
        ' Moto G8 : Motorola Mobility', ' Lite : Motorola Mobility', ' Motorola Edge Edge+ : Motorola Mobility',
        ' Moto G Pro : Motorola Mobility', ' Moto G Fast : Motorola Mobility',
        ' Motorola One : Motorola Mobility', ' Motorola One : Motorola Mobility',
        ' Moto G 5G Plus : Motorola Mobility', ' Moto G9 Play : Motorola Mobility',
        ' Moto G9 Plus : Motorola Mobility', ' Moto E7 Plus : Motorola Mobility',
        ' Motorola Razr : Motorola Mobility', ' Nexus S Samsung : Electronics Google',
        ' Galaxy Nexus Samsung : Electronics Google', ' Nexus 4 LG : Electronics Google',
        ' Nexus 5 LG : Electronics Google', ' Nexus 6 : Motorola', ' Nexus 5X LG : Electronics Google',
        ' Nexus 6P Huawei : Google', ' Nokia X : Nokia', ' Nokia XL : Microsoft Mobile',
        ' Nokia X2 : Microsoft Mobile', ' Nokia 6 : HMD Global', ' Nokia 3 : HMD Global',
        ' Nokia 5 : HMD Global', ' Nokia 7 : HMD Global', ' Nokia 8 : HMD Global', ' Nokia 2 : HMD Global',
        ' Nokia 7 Plus : HMD Global', ' Nokia 1 : HMD Global', ' Nokia 6.1 : HMD Global',
        ' Nokia 8 Sirocco : HMD Global', ' Nokia 3.1 : HMD Global', ' Nokia 5.1 Plus : HMD Global',
        ' Nokia 2.1 : HMD Global', ' Nokia 5.1 : HMD Global', ' Nokia 6.1 Plus : HMD Global',
        ' Nokia 3.1 Plus : HMD Global', ' Nokia 7.1 : HMD Global', ' Nokia 8.1 : HMD Global',
        ' Nokia 9 PureView : HMD Global', ' Nokia 1 Plus : HMD Global', ' Nokia 4.2 : HMD Global',
        ' Nokia 3.2 : HMD Global', ' Nokia 2.2 : HMD Global', ' Nokia 6.2 : HMD Global',
        ' Nokia 7.2 : HMD Global', ' Nokia 2.3 : HMD Global', ' Nokia C1 : HMD Global',
        ' Nokia C2 : HMD Global', ' Nokia 1.3 : HMD Global', ' Nokia 5.3 : HMD Global',
        ' Nokia 8.3 5G : HMD Global', ' OnePlus One : OnePlus', ' OnePlus 2 : OnePlus', ' OnePlus X : OnePlus',
        ' OnePlus 3 : OnePlus', ' OnePlus 3T : OnePlus', ' OnePlus 5 : OnePlus', ' OnePlus 5T : OnePlus',
        ' OnePlus 6 : OnePlus', ' OnePlus 6T : OnePlus', ' OnePlus 7 : OnePlus', ' OnePlus 7 Pro : OnePlus',
        ' OnePlus 7T : OnePlus', ' OnePlus 7T Pro : OnePlus', ' OnePlus 8 : OnePlus',
        ' OnePlus 8 Pro : OnePlus', ' OnePlus Nord : OnePlus', ' Oppo N1 : Oppo', ' Oppo R7 : Oppo',
        ' Oppo F1 : Oppo', ' Oppo R11 : Oppo', ' Oppo F7 : Oppo', ' Oppo R15 Pro : Oppo', ' Oppo Find X : Oppo',
        ' Oppo F9 : Oppo', ' Oppo R17 : Oppo', ' Oppo Reno : Oppo', ' Oppo Reno2 : Oppo', ' Oppo A9 : Oppo',
        ' Oppo Find X2/Pro : Oppo', ' Pixel/XL : Google', ' Pixel 2/XL : Google', ' Pixel 3/XL : Google',
        ' Pixel 3a/XL : Google', ' Pixel 4/XL : Google', ' Pixel 4a : Google', ' Razer Phone : Razer Inc.',
        ' Razer Phone 2 : Razer Inc.', ' Redmi 1 : Xiaomi', ' Redmi 1S : Xiaomi', ' Redmi Note : Xiaomi',
        ' Prime : Xiaomi', ' Redmi 2 : Xiaomi', ' Redmi 2A : Xiaomi', ' Redmi 2 Prime : Xiaomi',
        ' Redmi Note 2 : Xiaomi', ' Redmi 2 Pro : Xiaomi', ' Redmi Note 3', ' Xiaomi Redmi 3 : Xiaomi',
        ' Redmi Note 3/Pro : Xiaomi', ' Redmi 3 Pro : Xiaomi', ' Redmi 3S : Xiaomi', ' Redmi 3X : Xiaomi',
        ' Redmi 3S Prime : Xiaomi', ' Xiaomi Redmi Note 4 : Xiaomi', ' Xiaomi Redmi Note 4/4X : Xiaomi',
        ' Xiaomi Redmi Note 5A/Prime : Xiaomi', ' Xiaomi Redmi 5/5 Plus : Xiaomi', ' Redmi Note 5 Pro : Xiaomi',
        ' Redmi Note 5 : Xiaomi', ' Xiaomi 6 Pro : Xiaomi', ' Redmi Note 6 Pro : Xiaomi',
        ' Redmi Note 7 : Xiaomi', ' Redmi Go : Xiaomi', ' Redmi Note 7 Pro : Xiaomi', ' Redmi 7A : Xiaomi',
        ' Redmi K20/Pro : Xiaomi', ' Redmi Note 8/Pro : Xiaomi', ' Xiaomi Redmi Note 8T',
        ' Xiaomi Redmi K30/5G : Xiaomi', ' Xiaomi Redmi Note 9 Pro /Pro Max/9S : Xiaomi',
        ' Redmi K30 Pro/Pro Zoom : Xiaomi', ' Redmi Note 9/Pro : Xiaomi', ' Xiaomi 10 : Xiaomi',
        ' Xiaomi Redmi K30 Ultra : Xiaomi', ' Samsung Galaxy : Samsung Electronics',
        ' Samsung Galaxy S1 : Samsung Electronics', ' Samsung Galaxy S2 : Samsung Electronics',
        ' Samsung Galaxy Note : Samsung Electronics', ' Samsung Galaxy S3 : Samsung Electronics',
        ' Samsung Galaxy Note 2 : Samsung Electronics', ' Samsung Galaxy S4 : Samsung Electronics',
        ' Samsung Galaxy S4 Zoom : Samsung Electronics', ' Samsung Galaxy Note 3 : Samsung Electronics',
        ' Samsung Galaxy Note 3 Neo : Samsung Electronics', ' Samsung Galaxy S5 : Samsung Electronics',
        ' Samsung Galaxy Grand Prime : Samsung Electronics', ' Samsung Galaxy Note 4 : Samsung Electronics',
        ' Samsung Galaxy Note Edge : Samsung Electronics', ' Samsung Galaxy S6 : Samsung Electronics',
        ' Samsung Galaxy Note 5 : Samsung Electronics', ' Samsung Galaxy S6 Edge+ : Samsung Electronics',
        ' Samsung Galaxy S7 : Samsung Electronics', ' Samsung Galaxy Note 7 : Samsung Electronics',
        ' Samsung Galaxy S8 : Samsung Electronics', ' Samsung Galaxy Note FE : Samsung Electronics',
        ' Samsung Galaxy Note 8 : Samsung Electronics', ' Samsung Galaxy S9 : Samsung Electronics',
        ' Samsung Galaxy Note 9 : Samsung Electronics', ' Samsung Galaxy S10 : Samsung Electronics',
        ' Samsung Galaxy S10 5G : Samsung Electronics', ' Samsung Galaxy Note 10 : Samsung Electronics',
        ' Samsung Galaxy Fold : Samsung Electronics', ' Samsung Galaxy Z Flip : Samsung Electronics',
        ' Samsung Galaxy S20 : Samsung Electronics', ' Galaxy Z Flip 5G : Samsung Electronics',
        ' Samsung Galaxy Note 20 : Samsung Electronics', ' Samsung Galaxy Z Fold 2 : Samsung Electronics',
        ' Sony Ericsson Xperia X10 : Sony Ericsson', ' : Sony Ericsson Xperia X8 : Sony Ericsson',
        ' Ericsson Xperia Play : Sony Ericsson', ' Xperia pro : Sony Ericsson', ' Sony Xperia Z : Sony Mobile',
        ' Sony Xperia Z Ultra : Sony Mobile', ' Sony Xperia Z1 : Sony Mobile',
        ' Sony Xperia Z1 Compact : Sony Mobile', ' Sony Xperia Z2 : Sony Mobile',
        ' Sony Xperia Z3 Compact : Sony Mobile', ' Sony Xperia Z4 : Sony Mobile',
        ' Sony Xperia Z5 Compact : Sony Mobile', ' Sony Xperia Z5 Premium : Sony Mobile',
        ' Sony Xperia X Performance : Sony Mobile', ' Sony Xperia XA : Sony Mobile',
        ' Sony Xperia XA Ultra : Sony Mobile', ' Sony Xperia X Compact : Sony Mobile', ' Sony Xperia XZ : Sony Mobile',
        ' Sony Xperia XZs Premium : Sony Mobile', ' Sony Xperia XA1 : Sony Mobile', ' Sony Xperia L1 : Sony Mobile',
        ' Sony Xperia XZ1 Compact : Sony Mobile', ' Sony Xperia L2 : Sony Mobile',
        ' Sony Xperia XZ2 Compact : Sony Mobile', ' Sony Xperia XZ2 Premium : Sony Mobile',
        ' Sony Xperia XZ3 : Sony Mobile', ' Sony Xperia 10 Plus : Sony Mobile', ' Xperia L3 : Sony Mobile',
        ' Sony Xperia 1 : Sony Mobile', ' Sony Xperia 5 : Sony Mobile', ' Sony Xperia 8 : Sony Mobile',
        ' Sony Xperia L4 : Sony Mobile', ' Sony Xperia 1 II : Sony Mobile', ' Sony Xperia 10 II : Sony Mobile',
        ' TCL 10 Pro Tecno', ' Tecno Spark 4/Air/Lite : Tecno Mobile', ' Tecno Camon 12 : Tecno Mobile',
        ' Tecno Camon 12 Pro : Tecno Mobile', ' Tecno Camon 12 Air : Tecno Mobile',
        ' Tecno Camon 15/Pro : Tecno Mobile', ' Tecno Camon 15 Air/Premier : Tecno Mobile',
        ' Tecno Mobile 10 : Tecno Mobile', ' Vivo X7 : Vivo', ' Vivo V9 : Vivo', ' Vivo NEX : Vivo',
        ' Vivo NEX 3 : Vivo', ' Vivo X50/Pro/Pro+ : Vivo', ' Xiaomi Mi 1 : Xiaomi', ' Xiaomi Mi 2 : Xiaomi',
        ' Xiaomi Mi 2S A : Xiaomi', ' Xiaomi Mi 3/3 TD : Xiaomi', ' Xiaomi Mi 4 : Xiaomi',
        ' Xiaomi Mi Note : Xiaomi', ' Xiaomi Mi Note Pro : Xiaomi', ' Xiaomi Mi 4i : Xiaomi',
        ' Xiaomi Mi 4c : Xiaomi', ' Xiaomi Mi 5 Xiaomi', ' Xiaomi Mi Note 2 : Xiaomi',
        ' Xiaomi Mi MIX : Xiaomi', ' Xiaomi Mi 5c : Xiaomi', ' Xiaomi Mi 5X/Mi A1 : Xiaomi',
        ' Xiaomi Mi MIX 2 : Xiaomi', ' Xiaomi Mi MIX 2S : Xiaomi', ' Xiaomi Mi 6X/Mi A2 : Xiaomi',
        ' Xiaomi Mi 8 : Xiaomi', ' Xiaomi Pocophone F1 : Xiaomi', ' Xiaomi Mi 8 Pro : Xiaomi',
        ' Xiaomi Mi MIX 3 : Xiaomi', ' Xiaomi Mi 9 : Xiaomi', ' Xiaomi Mi MIX 3 5G : Xiaomi',
        ' Xiaomi Mi 9T : Xiaomi', ' Xiaomi Mi A3 : Xiaomi', ' Xiaomi Mi 9T Pro : Xiaomi',
        ' Xiaomi Mi 9 Pro/Pro 5G : Xiaomi', ' Xiaomi Mi Note 10/Pro : Xiaomi', ' Xiaomi Mi 10/Pro : Xiaomi',
        ' POCO M2 Pro : Xiaomi', ' Xiaomi Mi 10 Ultra : Xiaomi', ' ZTE Racer : ZTE', ' ZTE Blade : ZTE')

    price = round(random.uniform(300, 3500), 1)
    return {
        'product_id': get_valid_product_id(),
        'product_name': product_name,
        'model': model,
        'maker': maker,
        'stock': random.randint(0, 99),
        'price': price,
    }


if __name__ == '__main__':
    for i in range(1):
        product = get_valid_product()
        insert_product(**product)
        print(f'Product ID: #{product["product_id"]} Name:'
              f'{product["product_name"]} {product["model"]} {product["maker"]} Inserted')
