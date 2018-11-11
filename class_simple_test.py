#checking He/She is Good or Bad

class Attitude_check:

    def Defense_check(self):
        print("################# Personality Checker #########################")
        print("Enter all the Percentage within 100%")
        name = input("Enter a Person Name:")
        age = input("Enter a Age:")
        thinking_attitude_percen = int(input("Enter a Thinking ability of person:"))
        speaking_attitude_percen = int(input("Enter a Speaking ability of person:"))
        working_attitude_percen = int(input("Enter a Working ability:"))

        if thinking_attitude_percen >= 65 and speaking_attitude_percen >= 45 and working_attitude_percen >= 75:
            print("{x} is Good person assured by INFIDOS".format(x=name))
        else:
            print("{x} is Bad person assured by INFIDOS".format(x=name))


attitude = Attitude_check()
attitude.Defense_check()
