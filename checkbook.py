# %%
def main():
    ''' 
    
    '''
    print("------ Welcome to your terminal checkbook!-----")
    main_page()

    print("\nThe End")
    print(f"Try again, it closes weird sometimes")
    return


# %%
def main_page():
    ''' 
    functin will start adventure and give players two choices, chosen option will print out
    '''

    transactions = len(list(ledger.values())[0])


    recent_balance = ledger["resulting_balance"][(transactions-1)]
    w = widgets.HTML(value = (str(recent_balance)),placeholder = "p-h",description = "Current Balance:")
    display(w)


    print("1) View ledger")
    print("2) record a debit (withdraw)")
    print("3) record a credit (deposit)")
    print("4) exit and save changes")
    print("5) working on it")
    
    door_picked = input("What would you like to do > ").lower()

    #door_picked should be a string of response
    if door_picked == "1":
        view_ledger()
    elif door_picked == "2":
        record_debit()
    elif door_picked == "3":
        record_credit()
    elif door_picked == "4":
        exit()
    elif door_picked == "5":
        hidden_function()
    else:
        print("Sorry, please pick 1 through 4.")

# %%
def hidden_function():
    from ipywidgets import widgets  

    # Create text widget for output
    output_text = widgets.Text()

    # Create text widget for input
    input_text = widgets.Text(
        value='Transaction Amount (Credit, no symbols please)',
        placeholder='Numerical',
        description='Spent',
        disabled=False
    )
    describe_text = widgets.Text(
        value='Description',
        placeholder='Text',
        description='Desc-Spent',
        disabled=False
    )
    date_text = widgets.Text(
        value='DD/MM/YYYY HH:MM',
        placeholder='date',
        description='DD/MM/YYYY HH:MM',
        disabled=False
    )

    # Define function to bind value of the input to the output variable 
    def bind_input_to_output(sender):
        print(sender.value)
        sender.value=""
        #output_text.value = input_text.value
        #print(output_text.value)

    # Tell the text input widget to call bind_input_to_output() on submit
    input_text.on_submit(bind_input_to_output)
    describe_text.on_submit(bind_input_to_output)
    date_text.on_submit(bind_input_to_output)

    # Display input text box widget for input
    display(input_text,describe_text,date_text)

            
    main_page()

# %%
def view_ledger():
    import ipywidgets as widgets
    from ipywidgets import interactive,interact
    
    number = ['All']+(list(ledger["transaction_number"]))
    
    def view(x=''):
        if x=='All':
            print(list(ledger.keys()))
            for i in  range(len(list(ledger.values())[0])):
                print('{:>10s}{:>20s}{:>25s}{:>30s}{:>30s}'.format(str(list(ledger.values())[0][i]),\
                        str(list(ledger.values())[1][i]),\
                        str(list(ledger.values())[2][i]),\
                        list(ledger.values())[3][i],\
                        list(ledger.values())[4][i]))
            return
        else:
            return print(list(ledger.values())[0][x-1],"<-Transaction Number"),\
                    print(list(ledger.values())[1][x-1],"<-Resulting Balance"),\
                    print(list(ledger.values())[2][x-1],"<-Transaction Amount"),\
                    print(list(ledger.values())[3][x-1],"<-Transaction Description"),\
                    print(list(ledger.values())[4][x-1],"<-Transaction Timestamp"),\
        
    w = widgets.Select(options=number)
    #interactive(view, x=w)
    interact(view, x=w)

    exit()

# %%
def record_debit():
    print("adding debit")

    ttl_rows=int(len(ledger["transaction_number"]))

    ledger["transaction_number"].append(ttl_rows+1)

    debit = float(input("How much did you spend (only decimal and numbers)"))
    ledger["resulting_balance"].append(float(ledger["resulting_balance"][(ttl_rows-1)])-debit)
    ledger["transaction_amount"].append(float(debit * -1))

    descript = input("small description (<15 char)")
    ledger["transaction_description"].append(descript)

    date_time = input("DD/MM/YYYY HH:MM (approx)")
    ledger["transaction_timestamp"].append(date_time)


# %%
def record_credit():
    "adding credit"

    ttl_rows=int(len(ledger["transaction_number"]))

    ledger["transaction_number"].append(int(len(ledger["transaction_number"])+1))

    credit = float(input("How much did you make (only decimal and numbers)"))
    ledger["resulting_balance"].append(float(ledger["resulting_balance"][(ttl_rows-1)])+credit)
    ledger["transaction_amount"].append(float(credit))

    descript = input("small description (<15 char)")
    ledger["transaction_description"].append(descript)

    date_time = input("DD/MM/YYYY HH:MM approx")
    ledger["transaction_timestamp"].append(date_time)
                
    main_page()


# %%
def exit():

    with open("transaction_history.txt", 'w') as f: 
        for key, value in ledger.items(): 
            f.write('%s:%s\n' % (key, value))  
# %%
def initialize_account():
    ''' 
    when starting account
    '''
    if os.path.exists(main_path+'/transaction_history.txt'):
        with open('transaction_history.txt','r') as f: 
            myvariable = f.readlines()
            ledger={k:[] for k in [keyed.split(":")[0] for keyed in myvariable]}
            for each in range(len([keyed.split(":")[1] for keyed in myvariable][0].strip("[").split("]")[0].split(","))):
                ledger["transaction_number"].append(int([keyed.split(":")[1] for keyed in myvariable][0].strip("[").split("]")[0].split(",")[each]))
                ledger["resulting_balance"].append(float([keyed.split(":")[1] for keyed in myvariable][1].strip("[").split("]")[0].split(",")[each]))
                ledger["transaction_amount"].append(float([keyed.split(":")[1] for keyed in myvariable][2].strip("[").split("]")[0].split(",")[each]))
                ledger["transaction_description"].append(str([keyed.split(":")[1] for keyed in myvariable][3].strip("[").split("]")[0].split(",")[each].split("'")[1]))
                ledger["transaction_timestamp"].append([keyed.split(":",1)[1] for keyed in myvariable][4].strip("[").split("]")[0].split(",")[each].split("'")[1])
    else:
        ledger={k:[] for k in [ "transaction_number", 
                                "resulting_balance", 
                                "transaction_amount",
                                "transaction_description",
                                "transaction_timestamp"]}
        print("We can't find an account for you, so we'll start one! We'll even add a dollar to your account!")

        ledger["transaction_number"].append(1)
        ledger["resulting_balance"].append(1)
        ledger["transaction_amount"].append(1)
        ledger["transaction_description"].append("thanks for joining")
        ledger["transaction_timestamp"].append("01/01/01 12:00")
        
    return ledger


# %%
from ipywidgets import widgets
import os

main_path=os.getcwd()

if __name__ == "__main__":
    ##look for file or else create one
    ledger = initialize_account()

    #widgets.GridBox(personal_inventory,layout = widgets.Layout(grid_template_columns="repeat(3, 100px)"))
    main()



# %%
