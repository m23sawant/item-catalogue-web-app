
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name=" GOD", email="god@gmail.com")
session.add(User1)
session.commit()

category1 = Categories(user_id=1, name="Football")
session.add(category1)
session.commit()


category2 = Categories(user_id=1, name="Basketball")
session.add(category2)
session.commit()

category3 = Categories(user_id=1, name="Baseball")
session.add(category3)
session.commit()

category4 = Categories(user_id=1, name="Cricket")
session.add(category4)
session.commit()

category5 = Categories(user_id=1, name="Tennis")
session.add(category5)
session.commit()

category6 = Categories(user_id=1, name="Track and Field")
session.add(category6)
session.commit()

category7 = Categories(user_id=1, name="Combat Sports")
session.add(category7)
session.commit()

category8 = Categories(user_id=1, name="Water Sports")
session.add(category8)
session.commit()

category9 = Categories(user_id=1, name="Hiking and Trekking")
session.add(category9)
session.commit()

category10 = Categories(user_id=1, name="Quidditch")
session.add(category10)
session.commit()

category11 = Categories(user_id=1, name="Gym and Fitness")
session.add(category11)
session.commit()


# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="NIKE Football",
                             description="The NIKE reacts football laser multicolour with vibrant graphics and construction that holds its shape.The NIKE react football comes with excellent touch and high visibility on the field. 26-panel design enhances ball flight.Butyl bladder provides strong rebound qualities and air retention. High-contrast graphics pattern gives a true read on trajectory and spin.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Football Studs",
                             description="Nivia Encounter 2.0 delivers enhanced grip and stability while you enjoy your favourite sport. You can use these studs for your daily practice sessions. They have a sole made from premium quality material for enhanced durability. Nivia is known for manufacturing top grade sports products. They offers an exclusive range of designs with top grade construction.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Basketball Ball",
                             description="The new and improved PU composite material has a much softer feel and smoother grip. There is aded tack covering so whether you are indoors or outdoors, this new material will help give you better control of the ball and the soft feel and the soft feel is great for passing. The improved durability of the PU synthetic can also be attributed to being more biodegradable than previous PVC materials and better for environment.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Slam Dunk Hoop Set",
                             description="Backboard hoop set with mini-basketball; Team logo printed on front; Dimensions: 12 x 9. Hangs on any door with padded hooks.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Baseball Bat",
                             description="SLYK Aluminum Youth Baseball Bat made from high grade Aluminum alloy for faster swing speed. ultra-thin handle with All Sports grip for increased stability and accuracy, Ideal for all levels of baseball players from practice to matches. Specify the length and weight of bat in this bullet an ideal holiday gift for your budding baseball star!!! so grab yours right now!!",
                             categories=category3)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Baseball Glove",
                             description="The item you are looking at is a baseball gloves . This glove is used excellent condition. No holes or tears and stitching is all intact. It has the Ultra Soft lining. Thanks for looking. Any questions please ask.",
                             categories=category3)
session.add(categoryItem1)
session.commit()


session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Leather Cricket Ball",
                             description="The bullet is two-piece cricket ball made from quality alum tanned leather, it is ideally suited for club and school matches, water-proofed, quality centre construction encased with layers of quality portuguese cork wound with 100% wool, naturally seasoned inner core,long lasting",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Tennis Racquet",
                             description="If you are looking for a great sport to get your kid involved in then tennis is that sport. But finding the perfect racquet for your 8-10 year old can be tough. It is made easier with the Cosco Tennis Racquet range. Highlighted feature, One of the best highlights of the Cosco Tennis Racquet 25 is its string pattern which gives the racquet its power despite it light metal frame, Aluminum Make: Made from Aluminium the Cosco Tennis Racquet 25 looks visually attractive and is also sturdy and durable. It will not break or crack easily from tough or hard use.Lightweight:Its lightweight offers kids the right ammunition to manipulate the racquet. It gives more power and speed while swinging to hit the ball over the net.",
                             categories=category5)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Tennis Ball",
                             description="The Cosco All Court Tennis Ball is versatile as it can be used quite successfully on all types of courts -grassy, wet or hard court surfaces. Materials and fibers:The Cosco All Court Tennis Ball has interlocking fibers in the outer material which provides high durability and gives you an edge to deliver powerful shots. The shots are also well controlled. This, in turn, will give you consistency to your performance.It gives an amazing bounce suitable for hard courts as well. It is very light weighted and makes a great practice ball for kids.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Track & Field Shoes",
                             description="The skylite flyknit track & field shoe fitting like a second skin and the spikes upper is designed from single threads of yarn that are precisely engineered and significantly reduce waste for a virtually seamless fit. The tpu spike plate features a custom shank, offering snap and response on the track. This shoe is ideal for mid distance.(800mtr. to a500mtr.) (1) Flyknit upper lightweight and breathable. (2) Eva midsole -thin eva wedge for lightweight cushioning to keep your feet comfortable. (3) Rubber out sole- Durable rubber out sole for traction. (4) TPU spikes plate with seven removable spikes for greats traction on avariety of surfaces.",
                             categories=category6)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Marker Cones",
                             description="IWIN Cones Having Unique Features as Bright colors and design for easy visibility, Educational and learning purpose,Meet International Standards,witches hat training cones If you wish to purchase sport goods stores in India",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Boxing Gloves",
                             description="Lew Signature Fitness Boxing Gloves That Have Been A Trusted Training Staple For More Than A Decade. Ideal For Boxing, Kickboxing And Fitness Class Group Workouts. Constructed Of A Durable Double-ply Cross-weave Vinyl With A Multi-ply, Layered, Shock Absorbing Sandwich Foam For Superior Hand, Wrist And Knuckle Protection. Extra Wide Wrap Around Hook-and-loop Wrist Closure For Fast, Convenient And Secure Fit Disclaimer: This is an exclusive product from (LEW). All rights reserved. All trade names are registered trademarks of respective manufacturers listed. Attention all sellers: You are not authorized to sell (LEW) products, you cannot use the brand name of (LEW). Any unlawful distribution of this product can lead to a legal matter.",
                             categories=category7)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Punching Bag",
                             description="This heavy bag is a product brought to you by AURION. Its a sandbag that helps in workout and body fitness. The material used in making this bag prevents rashes in your hand. The unfilled sandbag with cushion effect also prevents hand injuries while punching and working out on the equipment.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="SURFBOARD",
                             description="Made for Beginner surfers weighing less than 85 kg or Advanced surfers of less than 100 kg. Volume: 100 L. The surfboard for safely starting out and improving. Comes with a leash and three soft-edge fins. Reinforced construction for surf club use.",
                             categories=category8)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Pool Ball",
                             description="Made for play water polo with all the family.A light grip ball, perfect for learning to play water polo.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Hiking Shoes",
                             description="Made for Hiking in nature for half a day, in dry weather, on easy trails. For beginners.1st technical price, these children's shoes are both durable and light. The TR sole extends the lifespan of the product and improves the grip of the shoe on all types of surfaces.",
                             categories=category9)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Camp Tent",
                             description="Made for Hikers seeking to shelter from the sun, wind or light rain.A simple, compact and transportable shelter that is very easy to pitch with conventional tent poles.",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Broomstick",
                             description="Probably the most iconic piece of equipment for quidditch, the broomstick serves the purpose of being a handicap such as one-handed dribbling in basketball or using only your feet in association football. The player must stay mounted on their broomstick for every moment of play unless they have been hit with a bludger, in which case the player needs to dismount from their broom and return to their hoops.[12] To be mounted on the broomstick means that the player must hold the broom between their legs and not have it fully on the ground. It can be supported by their thighs or hands equally, just as long as it is not attached to their person nor fully resting on the ground. Because of it being a handicap, sometimes players do not play with the brooms.",
                             categories=category10)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Golden Snitch",
                             description="The Golden Snitch, often called simply the Snitch, is the third and smallest ball used in Quidditch.[2] It is a walnut-sized gold-coloured sphere with silver wings. It flies around the Quidditch field at high speeds, sometimes pausing and hovering in place. The Seeker's goal is to catch the Snitch before the other team's seeker, which is worth one-hundred and fifty points. The game can only end when the Snitch has been caught, or by mutual agreement of the two teams' Captains; the latter is very rare, however, as one team would have to lose.",
                             categories=category10)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Dumbbell",
                             description="Made for weight training and functional workouts such as cross training. Perfect for your fitness prep.A versatile dumbbell for bodybuilding movements and functional exercises (press-up-type exercises). Its hexagonal shape offers better stability. durable rubber to protect against impacts.",
                             categories=category11)
session.add(categoryItem1)
session.commit()
categoryItem1 = CategoryItem(user_id=1, name="Training Bar",
                             description="Made for weight training at home with dumbbells. This bar was developed by our weight training coaches and design team.2 kg threaded bar, compatible with 28 mm discs. The non-slip grip keeps your hands from slipping for complete safety when training.",
                             categories=category11)
session.add(categoryItem1)
session.commit()

session.add(categoryItem1)
session.commit()
print ("added category items!")
