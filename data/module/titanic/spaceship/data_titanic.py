import pandas as pd

df = pd.read_csv("test.csv", sep=',')

df_test = pd.DataFrame()

head_df = df.head(10)

print(head_df)
print(type(df))

print(df.tail())

print(df.sample(5))

print(df.columns)

head_df.columns = [i for i in range(13)]
print(head_df)

print(df[7:15])

sample = df.sample(5)
print(sample)

print(sample.index)
sample.index = list("qwert")
print(sample)
print(sample[:2])

print(sample.iloc[1])

print(sample)
sample = sample.reset_index()
print(sample)

print(df.Name)

print(df["Name"])

type(df["Name"])
print(type)

print(df["Name"][:3])
print(df["Name"].to_list())

print(df.shape)

print(df.info())


print(df.Age.notna())
df = df[df.Age.notna()]

print(df.HomePlanet.notna())
df = df[df.HomePlanet.notna()]

print(df.Cabin.notna())
df = df[df.Cabin.notna()]

print(df.ShoppingMall.notna())
df = df[df.ShoppingMall.notna()]

print(df.CryoSleep.notna())
df = df[df.CryoSleep.notna()]

print(df.Destination.notna())
df = df[df.Destination.notna()]

print(df.VIP.notna())
df = df[df.VIP.notna()]

print(df.FoodCourt.notna())
df = df[df.FoodCourt.notna()]

print(df.Spa.notna())
df = df[df.Spa.notna()]

print(df.Name.notna())
df = df[df.Name.notna()]

print(df.VRDeck.notna())
df = df[df.VRDeck.notna()]

print(df.RoomService.notna())
df = df[df.RoomService.notna()]

print(df.info())

print(head_df, df.tail(), df.sample(5))

print(df[["Age", "HomePlanet", "CryoSleep"]])

print(df["Age"].min())

print(df["Age"].max())

print(df["Age"].mean())

print(df[["Age", "CryoSleep"]].groupby("CryoSleep").agg({"Age": ["mean", "min", "max", "median"]}))

df.HomePlanet = df.HomePlanet.apply(lambda x: 1 if x == "Earth" else 0)
print(df.HomePlanet)

print(df[["Age", "CryoSleep", "HomePlanet"]][df.CryoSleep == "True"].groupby("HomePlanet").agg({"Age": ["describe"]}))


df = df.astype(str)






