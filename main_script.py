{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f1cf8713-55cf-48f8-a1ab-e7bbf516f414",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Is 2024-08-15 a holiday? True\n",
      "Holiday on 2024-08-15: Independence Day\n",
      "Holidays in January: {datetime.date(2024, 1, 1): \"New Year's Day\", datetime.date(2024, 1, 26): 'Republic Day'}\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "class Holidays2024:\n",
    "    def __init__(self):\n",
    "        self.holidays = {\n",
    "            datetime.date(2024, 1, 1): \"New Year's Day\",\n",
    "            datetime.date(2024, 1, 26): \"Republic Day\",\n",
    "            datetime.date(2024, 3, 29): \"Holi\",\n",
    "            datetime.date(2024, 4, 10): \"Ram Navami\",\n",
    "            datetime.date(2024, 5, 1): \"Labor Day\",\n",
    "            datetime.date(2024, 8, 15): \"Independence Day\",\n",
    "            datetime.date(2024, 10, 2): \"Gandhi Jayanti\",\n",
    "            datetime.date(2024, 10, 24): \"Dussehra\",\n",
    "            datetime.date(2024, 11, 12): \"Diwali\",\n",
    "            datetime.date(2024, 12, 25): \"Christmas Day\",\n",
    "        }\n",
    "\n",
    "    def is_holiday(self, date):\n",
    "        return date in self.holidays\n",
    "\n",
    "    def get_holiday(self, date):\n",
    "        return self.holidays.get(date, \"Not a holiday\")\n",
    "\n",
    "    def get_holidays_in_month(self, month):\n",
    "        return {date: name for date, name in self.holidays.items() if date.month == month}\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    holidays = Holidays2024()\n",
    "    date_to_check = datetime.date(2024, 8, 15)\n",
    "    result_is_holiday = \"Is \" + str(date_to_check) + \" a holiday? \" + str(holidays.is_holiday(date_to_check))\n",
    "    result_get_holiday = \"Holiday on \" + str(date_to_check) + \": \" + holidays.get_holiday(date_to_check)\n",
    "    result_get_holidays_in_month = \"Holidays in January: \" + str(holidays.get_holidays_in_month(1))\n",
    "    \n",
    "    print(result_is_holiday)\n",
    "    print(result_get_holiday)\n",
    "    print(result_get_holidays_in_month)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a05e2f04-8a14-4602-8ba5-0f902037f992",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'holidays_2024'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mholidays_2024\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Holidays2024\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mdatetime\u001b[39;00m\n\u001b[0;32m      4\u001b[0m holidays \u001b[38;5;241m=\u001b[39m Holidays2024()\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'holidays_2024'"
     ]
    }
   ],
   "source": [
    "from holidays_2024 import Holidays2024\n",
    "import datetime\n",
    "\n",
    "holidays = Holidays2024()\n",
    "date_to_check = datetime.date(2024, 8, 15)\n",
    "print(\"Is \" + str(date_to_check) + \" a holiday? \" + str(holidays.is_holiday(date_to_check)))\n",
    "print(\"Holiday on \" + str(date_to_check) + \": \" + holidays.get_holiday(date_to_check))\n",
    "print(\"Holidays in January: \" + str(holidays.get_holidays_in_month(1)))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08f2f278-fe45-4352-af70-81c3e4c67c17",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
