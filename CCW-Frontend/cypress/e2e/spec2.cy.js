//Login in Tests
//Tests: page visit, right, wrong, empty
describe('Login Tests', () => {
  //Test 1: Does Login Page open? 
  it('Test 1: Login page opens', () => 
  {
    cy.visit('http://localhost:3000/'); 
    cy.get('[href="/login"]').click();

    // does URL change to the login page 
    cy.url().should('include', 'http://localhost:3000/login'); 
  });

  //Test 2: Does Login Page login with right credentials?
  it('Test 2: Login Page can login in using right credentials', () => 
  {
    cy.visit('http://localhost:3000/'); 
    cy.get('[href="/login"]').click(); 
    
    // Check if the URL changes to the login page
    cy.url().should('include', 'http://localhost:3000/login'); 

    //Valid credentials must work
    cy.get('#input-3').type('nxp330@case.edu');
    cy.get('#input-5').type('Neha0315!');

    //click submit button
    cy.get('.v-form > .v-btn').click(); 

    //Expected URL
    cy.url().should('include', 'http://localhost:3000/tracking'); 
  });

  //Test 3: Does Login Page login in using wrong credentials?
  it('Test 3: Login Page does not login in using wrong credentials', () => 
  {
     cy.visit('http://localhost:3000/'); 
     cy.get('[href="/login"]').click();

    // does URL change to the login page 
    cy.url().should('include', 'http://localhost:3000/login');

    //Invalid credentials shouldn't work
    cy.get('#input-3').type('nhy123@case.edu');
    cy.get('#input-5').type('Hello1234!');
    cy.get('.v-form > .v-btn').click();

    //error message needs to be present; doesn't work(need to be implemented still)
    //cy.get('.error-message').should('be.visible');

  });

  //Test 4: Does Login Page  login with empty parameters(credentials)?
  it('Test 4: Login Page does not login with empty credentials', () => 
  {
     cy.visit('http://localhost:3000/'); 
     cy.get('[href="/login"]').click();

    // does URL change to the login page 
    cy.url().should('include', 'http://localhost:3000/login');

    //Empty credentials shouldn't work
    cy.get('#input-3').should('not.have.text', '');
    cy.get('#input-5').should('not.have.text', '');
    cy.get('.v-form > .v-btn').click();

    //error message needs to be present; doesn't work(need to be implemented still)
    cy.get('.error-message').should('be.visible');

  });

});

/************************************************************************************************ */

//Register Tests
//Test: page visit, right, wrong, empty

describe('Register Tests', () => 
{
  //Test 1: Does register page open?
  it('Test 1: Register Page Opens', () => 
  {
    cy.visit('http://localhost:3000/'); 
    cy.get('.v-main > .v-btn').click();

    // does URL change to the login page 
    cy.url().should('include', 'http://localhost:3000/register'); 
  });

  //Test 2: Does it register new user with valid case id?
  it('Test 2: Registers User with Valid Case id', () => 
  {
    cy.visit('http://localhost:3000/'); 
    cy.get('.v-main > .v-btn').click();

    // does URL change to the login page 
    cy.url().should('include', 'http://localhost:3000/register'); 

     //check is user is old or new, if new then add to DB; if not give message

     //Valid credentials must work
    cy.get('#input-3').type('nxp330@case.edu');
    cy.get('#input-5').type('nxp330');
    cy.get('#input-7').type('Neha0315!');
    cy.get('#input-9').type('Neha0315!');

    //click submit button
    cy.get('.v-form > .v-btn').click(); 

    //Expected URL
    cy.url().should('include', 'http://localhost:3000/tracking'); 

  });

  it('Should not register old user', () => 
  {
    cy.visit('http://localhost:3000/'); 
    cy.get('.v-main > .v-btn').click();

    // does URL change to the login page 
    cy.url().should('include', 'http://localhost:3000/register');
    
    
    //check is user is old or new, if new then add to DB; if not give message
    //check if case id is valid 
    cy.get('#input-3').type('baby1230@case.edu');
    cy.get('#input-5').type('baby123');
    cy.get('#input-7').type('Happy324!');
    cy.get('#input-9').type('Happy324!');

    //error message needs to be present; doesn't work(need to be implemented still)
    //cy.get('.error-message').should('be.visible');

  });

});

/************************************************************************************************ */

//Tracking Page 
//Tests: page visit, add new search, delete, no classes, some classes, many classes   
describe('Tracking Page Tests', () => 
{
  //Test 1: Does register page open?
  it('Test 1: Tracking Page Opens from Login Page', () => 
  {
    //Using right login to access tracking page
    cy.visit('http://localhost:3000/'); 
    cy.get('[href="/login"]').click(); 
    
    // Check if the URL changes to the login page
    cy.url().should('include', 'http://localhost:3000/login'); 

    //Valid credentials must work
    cy.get('#input-3').type('nxp330@case.edu');
    cy.get('#input-5').type('Neha0315!');

    //click submit button
    cy.get('.v-form > .v-btn').click(); 

    //Expected URL
    cy.url().should('include', 'http://localhost:3000/tracking'); 
  });

  //Test 2: Does new search button work?
  it('Test 2: New Search Button works', () => 
  {
    //Using right login to access tracking page
    cy.visit('http://localhost:3000/'); 
    cy.get('[href="/login"]').click(); 
    
    // Check if the URL changes to the login page
    cy.url().should('include', 'http://localhost:3000/login'); 

    //Valid credentials must work
    cy.get('#input-3').type('nxp330@case.edu');
    cy.get('#input-5').type('Neha0315!');

    //click submit button
    cy.get('.v-form > .v-btn').click(); 

    //Expected URL
    cy.url().should('include', 'http://localhost:3000/tracking'); 

    //click add new search
    cy.get('.center-below').click();

    //keep counter of number of classes added 
    //once add new one then add to num
    //add new element
    cy.get('tbody > :nth-child(1) > :nth-child(1)')
    cy.get('tbody > :nth-child(2) > :nth-child(1)')
    cy.get('tbody > :nth-child(3) > :nth-child(1)')
    cy.get('tbody > :nth-child(4) > :nth-child(1)')

  });

  //Test 3: Does delete button work?
  it('Test 3: Delete Button works', () =>
  {


  }
  
  );

  //Test 4: Does list hold no classes(min)?
  it('Test 4: Min number of classes held in tracking list', () =>
  {


  }
  
  );

  //Test 5: Can list hold some classes(mid)?
  it('Test 5: Middle number of classes held in tracking list', () =>
  {


  }
  
  );

  //Test 6: Can list hold many classes(max)?
  it('Test 6: Max number of classes held in tracking list', () =>
  {


  }
  
  );

});


/************************************************************************************************ */

//Select Classes Page Page
//Tests: page visit, add new search, delete, no classes, some classes, many classes
describe('Select Classes Page Tests', () => 
{
  //Test 1: Does Select Classes page open?
  it('Test 1: Select classes opens', () =>
  {

  }
  
  );

});