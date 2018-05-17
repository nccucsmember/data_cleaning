
# coding: utf-8

# In[9]:


import csv
import codecs


fr = open('./1062_courses_all.csv', 'r')
data = csv.reader(fr)


written = []
i = 0
for row in data:
    written.append(row)
    written[i] = list(map(lambda s: s.strip(), written[i]))
    
    
    if i >= 1:

        written[i][0] = i # course_id
        written[i][1] = 1062 # course_semester
        
        if written[i][8] != 'N/A':
            s = written[i][8].split(' ')[0]
            
            if s.find(',') == -1 and s.find('&') == -1:
                if len(s) >= 3:
                    written[i][8] = s[3:5] + ':10' # course_begin_time
                    written[i][9] = s[6:8] + ':00' # course_end_time
                    written[i][10] = s[:3].upper() + '.' # course_weekday
        else:
            written[i][9] = 'N/A'
            written[i][10] = 'N/A'
        
        written[i][13] = written[i][13].split('/')[0] # course_type
        written[i][14] = True if written[i][14] == '是' else False # is_general
        written[i][16] = True if written[i][16] == '是' else False # central_general

    i += 1
print('DB_0')
fw = open("./1062_courses_all_cleaned.csv","w")
w = csv.writer(fw)
w.writerows(written)
fw.close()
fr.close()
        

    

