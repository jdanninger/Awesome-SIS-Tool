import { reactive } from 'vue';

// Create a reactive object to store global variables
const globalState = reactive({
  myGlobalVariable: 'Hello from global!',
});

export default globalState;