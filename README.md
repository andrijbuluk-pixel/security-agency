# Security Agency Project

# Test User: Username - user, Password - user12345


### 1. Preparation of the database
First, you need to apply migrations to create a table structure in your database:
`python manage.py migrate`.

### 2. Downloading test data
If you have an initial data file, upload it so you don't start with a completely empty project:
`python manage.py loaddata initial-date.json`.

### 3. Creating an administrator
Create a superuser account to access the administration panel:
`python manage.py createsuperuser`.

## Data models
The system is based on the following entities:

1.Client: Accounting of customers of services.<br>
2.Guard: Database of guards with license expiration control.<br>
3.Object: Objects under supervision.<br>
4.Event: Registration of incidents and events at facilities.<br>
5.Contract: Documentation of cooperation with clients.<br>

## Basic functions


- List of customers, creation, view of details, deletion.
- Guard list, creation, license renewal, deletion.
- List of objects, creation, update, deletion.
- List of events, creation of new events.
- Creation of a contract for the object.



## Additional functions

- User Authorization (LoginRequiredMixin)
- Forms with validation
- Deleting objects with confirmation


## 
# Diagram BD

<img width="1275" height="901" alt="Діаграма без назви drawio" src="https://github.com/user-attachments/assets/c32b9356-a485-45f1-a909-911d23f6fece" />


## 
# Login
<img width="1919" height="918" alt="Знімок екрана 2026-05-25 205205" src="https://github.com/user-attachments/assets/4b95f8e7-3487-47c8-a42d-3e8021f6cd92" />
<img width="1901" height="907" alt="Знімок екрана 2026-05-25 205214" src="https://github.com/user-attachments/assets/bef67fc0-0dac-4306-82c4-89381e573245" />

## 
# Home
<img width="1911" height="912" alt="Знімок екрана 2026-05-25 205132" src="https://github.com/user-attachments/assets/8fa45c68-9e66-45b7-9529-93b42bc99929" />
<img width="1908" height="909" alt="Знімок екрана 2026-05-25 205141" src="https://github.com/user-attachments/assets/c4672fd5-bf54-4086-957a-9d1ff9ecb15f" />
<img width="1919" height="907" alt="Знімок екрана 2026-05-25 205342" src="https://github.com/user-attachments/assets/13247f41-8d96-442e-b091-51ce67e8e482" />

## 
# Guard
<img width="1918" height="915" alt="Знімок екрана 2026-05-25 205443" src="https://github.com/user-attachments/assets/e064ebfc-17da-48fd-a883-f2ecce59f238" />
<img width="1919" height="912" alt="Знімок екрана 2026-05-25 205452" src="https://github.com/user-attachments/assets/b25ebdfe-a2ab-429f-ac42-94d68d7439ae" />
<img width="1919" height="907" alt="Знімок екрана 2026-05-25 205517" src="https://github.com/user-attachments/assets/a0a7bcfa-2a4f-480e-8283-71d721a80fda" />
<img width="1919" height="913" alt="Знімок екрана 2026-05-25 205522" src="https://github.com/user-attachments/assets/92734a78-b657-4909-8a65-ca7e5daf6bba" />
<img width="1910" height="896" alt="Знімок екрана 2026-05-25 210354" src="https://github.com/user-attachments/assets/67873f5e-bbf9-4c26-8543-d153fc1c4943" />

## 
# Client
<img width="1919" height="919" alt="Знімок екрана 2026-05-25 205458" src="https://github.com/user-attachments/assets/e3c80e75-d722-4dba-a6b6-dab4fb3785cc" />
<img width="1919" height="916" alt="Знімок екрана 2026-05-25 205504" src="https://github.com/user-attachments/assets/20018762-22c5-4f60-856b-1db1517ae330" />
<img width="1919" height="909" alt="Знімок екрана 2026-05-25 205724" src="https://github.com/user-attachments/assets/b63092a7-6e07-4272-928a-003a4d299af9" />
<img width="1919" height="915" alt="Знімок екрана 2026-05-25 205733" src="https://github.com/user-attachments/assets/6d984014-71fd-4eec-bced-9de2a02c99c0" />
<img width="1919" height="905" alt="Знімок екрана 2026-05-25 210434" src="https://github.com/user-attachments/assets/95598c13-758d-4602-a66a-b814cc88c7b7" />

## 
# Object
<img width="1919" height="907" alt="Знімок екрана 2026-05-25 205836" src="https://github.com/user-attachments/assets/5f1945fa-26ee-46ec-a289-806b7b3ec175" />
<img width="1919" height="912" alt="Знімок екрана 2026-05-25 205845" src="https://github.com/user-attachments/assets/b155e5ae-71c5-416c-bf70-2219bdc12de4" />
<img width="1919" height="910" alt="Знімок екрана 2026-05-25 205854" src="https://github.com/user-attachments/assets/b369379b-5b2e-4b22-a7ca-90f4f975e1d7" />
<img width="1919" height="904" alt="Знімок екрана 2026-05-25 205900" src="https://github.com/user-attachments/assets/308b2c2a-c535-48bd-a9f5-4d3c63206fe8" />
<img width="1919" height="895" alt="Знімок екрана 2026-05-25 205946" src="https://github.com/user-attachments/assets/ed3bb5ff-792a-48c3-8cf3-5bc017e7d2e5" />
<img width="1919" height="903" alt="Знімок екрана 2026-05-25 205952" src="https://github.com/user-attachments/assets/70a5c6e0-70a1-480f-a29b-fc3bc088a941" />
<img width="1918" height="912" alt="Знімок екрана 2026-05-25 210502" src="https://github.com/user-attachments/assets/743787bc-c272-4efe-9dd2-b5ad256a77da" />

## 
# Event
<img width="1913" height="911" alt="Знімок екрана 2026-05-25 210037" src="https://github.com/user-attachments/assets/56170576-f757-4a91-8e90-67a0c2b007f5" />
<img width="1919" height="908" alt="Знімок екрана 2026-05-25 210044" src="https://github.com/user-attachments/assets/d9ec101c-65fb-45b3-a772-8c25e4b08c4b" />

## 
# Logout
<img width="1919" height="915" alt="Знімок екрана 2026-05-25 210610" src="https://github.com/user-attachments/assets/b4c5750c-43ae-47fe-8adc-ad493ee80457" />

Link to the deployed project -> https://security-agency-7puw.onrender.com
