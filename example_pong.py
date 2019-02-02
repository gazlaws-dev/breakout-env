import random
import itertools
from pong import Pong
from cv2 import VideoWriter, VideoWriter_fourcc, imshow, waitKey, imwrite

def simple_agent_1(env):
  if not env.started:
    return 1

  ball_pos = env.ball.center
  paddle_pos = env.paddle_1.center

  if paddle_pos[1] < ball_pos[1]:
    return 2
  else:
    return 3

    
vid = VideoWriter('demo_pong.avi', VideoWriter_fourcc(*"XVID"), float(30), (160, 210), False)

env = Pong({
    'max_step': 1000,
    'lifes': 7,
    'ball_speed': [5, -2],
    # 'ball_size': [5, 5],
    # 'ball_color': 200,
    # 'paddle_width': 50,
    'paddle_speed': 5
  })
  
for ep in range(1):
  obs = env.reset()
  for t in itertools.count():
    #action = random.randint(0, env.actions - 1)
    action_1 = simple_agent_1(env)
    obs, reward, done, _ = env.step(action_1)
    print('Epsoide: {}, Step: {}, Reward: {}, Done: {}'.format(ep, t, reward, done))
    
    imshow('obs', obs)
    waitKey(1)
    vid.write(obs)
    if done:
      break

vid.release()
