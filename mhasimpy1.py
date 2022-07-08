import simpy


def clock(env, name, tick):
    while True:
        print(name, env.now)
        assert isinstance(tick, object)
        yield env.timeout(tick)


env = simpy.Environment()
env.process(clock(env, 'fast', 0.5))
# <Process(clock) object at 0x>
env.process(clock(env, 'slow', 1))
# <Process(clock) object at 0x>
env.run(until=2)
