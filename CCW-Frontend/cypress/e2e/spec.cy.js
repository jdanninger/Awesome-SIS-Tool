describe('Home page test', () => 
{
  it('Home page exists', () => {
    cy.visit('http://localhost:3000/')
  })

  it('Home page elements exist', () => 
  {
    cy.visit('http://localhost:3000/')

    //title exists
    cy.get('.v-toolbar-title__placeholder > .v-btn > .v-btn__content')

    //main
    cy.get('.v-main')

    //picture present
    cy.get('.centered')

    //register button is present
    cy.get('.v-main > .v-btn')

    //toolbar is present
    cy.get('.v-toolbar__content')

    //login is present
    cy.get('[href="/login"]')
   
  })

 
})

describe('Login page test', () => {
  it('Login page elements exist', () => 
  {
    cy.visit('http://localhost:3000/login')
  })
})

describe('Register page test', () => {
  it('Register page elements exist', () => {
    cy.visit('http://localhost:3000/register')

  })
})

describe('Tracking page test', () => {
  it('Tracking page elements exist', () => {
    cy.visit('http://localhost:3000/tracking')

  })
})




