# [Nieghbourhood](https://backend-hood.herokuapp.com/)
# Neighbourhood
<table>
<tr>
<td>
  The backend of a neighbourhood application that keeps track of what happens in different neighbourhood
</td>
</tr>
</table>

## [Usage](https://backend-hood.herokuapp.com/)

### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

### Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/Nelly-ayebale/Neighbourhood/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/Nelly-ayebale/Neighbourhood/issues/new). Please include sample queries and their corresponding results.

## Authors
- [Kevin Ligare Ambundo](https://github.com/kevin3708)
- [Ayebale Nelly Abigail](https://github.com/Nelly-ayebale)

## Built with 

- Django(3.1.3)
- HTML
- CSS
- Bootstrap4

## To-do
- The application should have 3 sets of users i.e the System Administrator,The Neighbourhood Admin and the Normal users.
- All users can view the neighbourhoods but only the System Administrator and the Neighbourhood Admin can update the neighbourhoods.
- Only the System Administrator can create Neighbourhoods.
- Members(Normal Users) should be able to sign up and login the application.
- Join only one neighbourhood and post new posts onto the neighbourhood posts.
- The Neighbourhood Admin should be able to post Businesses and healthcentre numbers and police numbers.


## Resources
This website was helpful in extending the Django User Model[here](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)

## Admin Information
- Username : Ayebale
- Password : 1234

## API ENDPOINTS
- GET [To get Users]: https://backend-hood.herokuapp.com/userlist
- POST [To Post Neighbourhoods-Only for Admin and appointed Staff Members] :https://backend-hood.herokuapp.com/hood
- POST [To Post Businesses and their information- Only for Admin and appointed Staff Members] : https://backend-hood.herokuapp.com/business
- REGISTER [For All Users ] : https://backend-hood.herokuapp.com/auth/signup/
- LOGIN [For All Users ] : https://backend-hood.herokuapp.com/auth/login/

[MIT](LICENSE) ©

