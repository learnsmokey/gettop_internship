# Created by Vallikannu at 7/11/2022
Feature: Add products to wishlist, verify user sees correct products
  # Enter feature description here

  Scenario: Add and verify user sees correct product
    Given Open Gettop page
    When Click the heart icon
    Then Click on the browse wishlist
    Then Verify correct product is there


  Scenario: Add products to wishlist,verify user can remove products and sees a confirmation message
    Given Open Gettop page
    When Click the heart icon
    Then Click on the browse wishlist
    Then Verify correct product is there
    When Click on Remove this product button
    Then User see confirmation message


  Scenario: Add products to wishlist, verify user can click on wishlist item and is taken to correct product page
    Given Open Gettop page
    When Click the heart icon
    Then Click on the browse wishlist
    Then Verify correct product is there
    Then Click on wishlist item
    Then Confirm,taken to correct product page

  Scenario: User can see social logos to share wishlist items
    Given Open Gettop page
    When Click the heart icon
    Then Click on the browse wishlist
    Then User can see social logo to share