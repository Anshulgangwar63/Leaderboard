class User:
  def __init__(self, data):
    self.rank = 100000000
    print(data)
    self.name = data[0]
    self.UID = data[1]
    self.handle = data[2]
    self.contests = int(data[3])
    self.score = int(data[4])

  def __repr__(self):
    return {
      "rank": self.rank,
      "name": self.name,
      "UID": self.UID,
      "handle": self.handle,
      "contests": self.contests,
      "score": self.score
    }

  def __str__(self):
    return "Rank: " + str(self.rank) + "\nName: " + self.name + "\nUID: " + self.UID

  @property
  def user(self):
    return self.name + " @ " + self.handle