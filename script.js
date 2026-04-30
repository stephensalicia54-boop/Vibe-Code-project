const STORY_STATES = {
  start: {
    text: `Greetings stranger. It seems you have stumbled upon an old haunted house. You have two options here: walk away from the house and the haunting feeling it gives you, or enter the old abandoned house and discover why curiosity killed the cat.`,
    options: [
      { label: 'Walk away', next: 'walk_away' },
      { label: 'Enter The House', next: 'enter_house' },
    ],
    bgColor: '#2a2434',
    bgImage: 'images/haunted_house.png',
  },
  walk_away: {
    text: `Ending: Scaredy Cat. You chose to walk away from the haunted house, but as you leave, curiosity eats at you. You may live another day, yet your mind will forever wonder what could have happened inside.`,
    options: [{ label: 'Restart', next: 'start' }],
    bgColor: '#362b2d',
    bgImage: 'images/walk_away.png',
  },
  enter_house: {
    text: `You enter the haunted house. Thousands of eyes seem to watch you as you approach the door, but none look back. The door slams shut behind you, locking you inside. A gas fills the room and you pass out.`,
    options: [
      { label: 'Open Door One', next: 'door_one' },
      { label: 'Open Door Two', next: 'door_two' },
      { label: 'Open Door Three', next: 'door_three' },
    ],
    bgColor: '#1b1f28',
    bgImage: 'images/entry_hall.png',
  },
  door_one: {
    text: `Ending: Drop. Door One opens and something pushes you into a dark shaft. Wind rushes past your face as you fall, and you finally see the bottom of the pit.`,
    options: [{ label: 'Restart', next: 'start' }],
    bgColor: '#151820',
    bgImage: 'images/pit.png',
  },
  door_two: {
    text: `Ending: Trapped. Door Two locks behind you. No matter how hard you try, the door does not open. Hours or days pass before you finally succumb to your fate.`,
    options: [{ label: 'Restart', next: 'start' }],
    bgColor: '#241a1f',
    bgImage: 'images/trapped_room.png',
  },
  door_three: {
    text: `Door Three opens and pushes you through. The door slams behind you, and your eyes adjust to bright light. You see two levers and a sign that says one leads to freedom and one leads to doom.`,
    options: [
      { label: 'Pull Lever One', next: 'lever_one' },
      { label: 'Pull Lever Two', next: 'lever_two' },
    ],
    bgColor: '#2f2a32',
    bgImage: 'images/levers.png',
  },
  lever_one: {
    text: `Ending: Escape. You pull Lever One and hear a door slowly squeak open. Outside the threshold, the sun is rising and dew glitters on the grass. You run to safety and see the light of a new day.`,
    options: [{ label: 'Restart', next: 'start' }],
    bgColor: '#28322a',
    bgImage: 'images/sunrise.png',
  },
  lever_two: {
    text: `Ending: Bat. You pull Lever Two and hear metal springs. A baseball bat swings out and strikes you. This is a deadly ending you can only escape by restarting and choosing differently.`,
    options: [{ label: 'Restart', next: 'start' }],
    bgColor: '#301a1c',
    bgImage: 'images/bat_trap.png',
  },
};

const storyText = document.getElementById('storyText');
const choicesPanel = document.getElementById('choicesPanel');
const storyPanel = document.getElementById('storyPanel');
const storyOverlay = document.querySelector('.story-overlay');
let currentState = 'start';

function setScene(state) {
  const stateData = STORY_STATES[state];
  storyText.textContent = stateData.text;
  renderOptions(stateData.options);
  updateBackground(stateData, state);
}

function renderOptions(options) {
  choicesPanel.innerHTML = '';
  options.forEach((option) => {
    const button = document.createElement('button');
    button.className = 'choice-button';
    button.textContent = option.label;
    button.addEventListener('click', () => {
      currentState = option.next;
      setScene(currentState);
    });
    choicesPanel.appendChild(button);
  });
}

function updateBackground(stateData, state) {
  const bgImage = stateData.bgImage || '';
  const safeUrl = `url('${bgImage}')`;
  storyPanel.style.setProperty('--bg-color', stateData.bgColor);
  storyPanel.style.setProperty('--bg-image', bgImage ? safeUrl : 'none');

  if (state === 'enter_house') {
    storyOverlay.style.backgroundImage = "url('pickthreedoors.png')";
  } else {
    storyOverlay.style.backgroundImage = "url('Untitled design.png')";
  }
}

setScene(currentState);
