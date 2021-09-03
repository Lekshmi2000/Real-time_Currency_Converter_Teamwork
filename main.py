import requests
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("Real-time Currency Converter")
root.geometry("800x500")
frame1 = Frame(root, highlightbackground="black", highlightthickness=4,width=800, height=500, bd= 0)
frame1.pack()

photo = ImageTk.PhotoImage(Image.open("./currencyconverter.png"))
img_label = Label(frame1,image=photo)
img_label.pack()
Convert_from = Label(root,font=('Helvetica',17,'bold'),text = " Convert from: ",fg="black",borderwidth=1,relief="solid").place(x = 135,y = 100)
Convert_to = Label(root,font=('Helvetica',17,'bold'), text = " Convert to: ",fg="black",borderwidth=1,relief="solid").place(x = 500,y = 100)
User_from_entry_area = Entry(root,width = 18,font=('Helvetica',17,'bold'),bd=5,bg='#cce0ff')
User_from_entry_area.place(x = 100,y = 175)
User_to_entry_area = Entry(root,width = 18,font=('Helvetica',17,'bold'),bd=5,bg='#cce0ff')
User_to_entry_area.place(x = 460,y = 175)

Input = StringVar(root)
Output = StringVar(root)

Input.set("Select")
Output.set("Select")
Currecy_list = ['USD','EUR','JPY','BGN','CZK','DKK','GBP','HUF','PLN','RON','SEK','CHF','ISK','NOK','HRK','RUB','TRY','AUD','BRL','CAD','CNY','HKD','IDR','INR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR']
FromCurrency_option = OptionMenu(root,Input, *Currecy_list)
FromCurrency_option["menu"].config(bg='#cce0ff')
ToCurrency_option = OptionMenu(root,Output, *Currecy_list)
ToCurrency_option["menu"].config(bg='#cce0ff')
FromCurrency_option.place(x=180, y=270)
ToCurrency_option.place(x=550, y=270)


def CurrencyConversion():
    if (User_to_entry_area.get() == ""):

        Input_currency = Input.get()
        Output_currency = Output.get()
        if (User_from_entry_area.get() == ""):
            tkinter.messagebox.showerror("Error", "Enter your amount.\n")

        elif (Input_currency == "Select" or Output_currency == "Select"):
            tkinter.messagebox.showerror("Error", "Select currency.\n")

        else:

            api_key = "DGHU9BX2YDTSI6R5"
            base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
            main_url = base_url + "&from_currency=" + Input_currency +"&to_currency=" + Output_currency + "&apikey=" + api_key
            data = requests.get(main_url)
            data_value = data.json()
            Exchange_Rate = float(data_value["Realtime Currency Exchange Rate"]
                                  ['5. Exchange Rate'])
            amount = float(User_from_entry_area.get())
            new_amount = round(amount * Exchange_Rate, 3)
            User_to_entry_area.insert(0, str(new_amount))
    else:
        tkinter.messagebox.showerror("Error", "If you want to convert again, RESET and enter new amount.\n")


def Clear():
    User_from_entry_area.delete(0, END)
    User_to_entry_area.delete(0, END)
    Input.set("Select")
    Output.set("Select")


Convert_btn = Button(root, text = 'CONVERT',bg='#2EDBF2', bd = '5', command= CurrencyConversion,font=('Helvetica',13,'bold'))
Convert_btn.place(x=300, y=375)
Clear_btn = Button(root, text = ' CLEAR ',bg='#2EDBF2', bd = '5', command= Clear,font=('Helvetica',13,'bold'))
Clear_btn.place(x=435, y=375)



root.mainloop()


