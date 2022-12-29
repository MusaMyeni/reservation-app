# READ FIRST

The "Musa's BnB Reservation App" is an application built in response to a task that was given to me to complete. I have taken the liberty to create a miniature application using the below case, and hosted it on AWS' free tier for easy access.

The project was created from scratch (without using a template) and styled using Tailwind (using the django-tailwind package for easier integration)

Within the EC2 instance, I've installed Docker / Docker Compose and created a docker-compose.yml file which downloads an image of this project (which is automatically created/recreated using a Github Action, and hosted on GHCR.IO). Along with an NGINX image using the files also in the repository. 

The application can be found here: 

## Question
>Lets we have a django project.
>With models:
>
>Rental
> - name
>
>Reservation
>  - rental_id
>  - checkin(date)
>  - checkout(date)
>

>Add the view with the table of Reservations with "previous reservation ID".
>Previous reservation is a reservation that is before the current one into same rental.


>Example:
>Rental-1.  
>Res-1(2022-01-01, 2022-01-13)  
>Res-2(2022-01-20, 2022-02-10)  
>Res-3(2022-02-20, 2022-03-10)  

>Rental-2.  
>Res-4(2022-01-02, 2022-01-20)  
>Res-5(2022-01-20, 2022-02-11)  


>|Rental_name|ID      |Checkin    |Checkout  |Previous reservation, ID|

>|rental-1   |Res-1 ID| 2022-01-01|2022-01-13| -                      |  
>|rental-1   |Res-2 ID| 2022-01-20|2022-02-10| Res-1 ID               |  
>|rental-1   |Res-3 ID| 2022-02-20|2022-03-10| Res-2 ID               |  
>|rental-2   |Res-4 ID| 2022-01-02|2022-01-20| -                      |  
>|rental-2   |Res-5 ID| 2022-01-20|2022-01-11| Res-4 ID               |

>Also, add a tests.

>Write it in -- using the Django form solution. 
>Its  regular query, not database view.

>Create it into github repo and provide a link to it.


## Answer

Given the question above, i used a Lag function in order to achieve the desired result. I was, however, unclear if I should display the answer as a plain SQL Query using Django ORM notation, or via the frontend. So I did all three.

Via Frontend:

URL: [ec2-13-38-89-136.eu-west-3.compute.amazonaws.com](http://ec2-13-38-89-136.eu-west-3.compute.amazonaws.com/)   
USERNAME: admin@dummyaccount.com  
PASSWORD: #password123!  


Via SQL Query:
 
```SQL
SELECT  rnt.name, rsv.id, rsv.check_in, rsv.check_out, lag(rsv.id, 1) OVER (
    PARTITION BY rnt.id
    ORDER BY rsv.id ASC
  ) previous_reservation_id
FROM bookings_reservation rsv
LEFT JOIN bookings_rental rnt ON rnt.id = rsv.rental_id
```

Via Django ORM:


```Python
Reservation.objects.annotate(previous_reservation_id=Window(expression=Lag('id', 1), partition_by=[F('rental_id')], order_by=F('id').asc() )).values('rental_id__name', 'id', 'check_in', 'check_out', 'previous_reservation_id')
```

I also added a few tests as the question required.