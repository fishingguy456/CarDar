import glob, os, pathlib, shutil

dataset = pathlib.Path("C:/Users/qukev/OneDrive/Desktop/CarDar/dataset/car_data/car_data").as_posix()
test = pathlib.Path(dataset, "test").as_posix()

car_dirs = glob.glob(pathlib.Path(test, "*").as_posix())
validation = pathlib.Path(dataset, "validation").as_posix()
if not os.path.exists(validation):
    os.makedirs(validation)

for car_dir in car_dirs:
    cars = os.listdir(car_dir)
    validation_car = pathlib.Path(validation, os.path.split(car_dir)[1]).as_posix()
    if not os.path.exists(validation_car):
        os.makedirs(validation_car)
    if (len(os.listdir(validation_car)) == 0):
        for car in cars[:len(cars)//2+1]:
            shutil.move(pathlib.Path(car_dir, car).as_posix(), pathlib.Path(validation_car, os.path.basename(car)).as_posix())