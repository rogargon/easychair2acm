import pandas


def splitAuthors(authors_string):
    authors_string = authors_string.replace(' and ', ', ')
    authors_array = authors_string.split(', ')
    return [x for x in authors_array if "and" not in x]


def findAuthor(paper_id, fullname, authors):
    for row in authors.iterrows():
        submission = row[1][0]
        fname = row[1][1]
        sname = row[1][2]
        if fullname.startswith(fname) & fullname.endswith(sname) & (paper_id == submission):
            return row


def process_submissions(accepted, authors, output):
    print('proceedingID,event_tracking_number/theirnumber,paper_type,theTitle,prefix,first_name,middle_name,last_name,'
          + 'suffix,author_sequence_no,contact_author,ACM_profile_id,ACM_client_no,orcid,email,department_school_lab,'
          + 'institution / AFFILIATION,city,state_province,country,secondary_department_school_lab,'
          + 'secondary_institution,secondary_city,secondary_state_province,secondary_country,section_title,'
          + 'section_seq_no,published_article_number,start_page,end_page,article_seq_no,art_submission_date,'
          + 'art_approval_date,source (submission system),abstract', file=output)
    for submission in accepted.iterrows():
        subauthors = submission[1][2]
        authorlist = splitAuthors(subauthors)
        author_sequence = 1
        for author in authorlist:
            sid = submission[1][0]
            title = '"' + submission[1][1] + '"'
            author_record = findAuthor(sid, author, authors)
            prefix = ''
            first_name = author_record[1][1]
            middle_name = ''
            last_name = author_record[1][2]
            suffix = ''
            contact_author = author_record[1][8]
            ACM_profile_id = ''
            ACM_client_no = ''
            orcid = ''
            email = author_record[1][3]
            department_school_lab = ''
            institution = '"' + author_record[1][5] + '"'
            city = ''
            country = author_record[1][4]
            state_province = ''
            secondary_department_school_lab = ''
            secondary_institution = ''
            secondary_city = ''
            secondary_state_province = ''
            secondary_country = ''
            section_title = ''
            section_seq_no = ''
            published_article_number = ''
            start_page = ''
            end_page = ''
            article_seq_no = ''
            art_submission_date = ''  # submission[1][3]
            art_approval_date = ''
            source = 'Easychair'
            abstract = '"' + submission[1][10] + '"'
            print('proceedingID', sid, 'Full Paper', title, prefix, first_name, middle_name, last_name,
                  suffix, author_sequence, contact_author, ACM_profile_id, ACM_client_no, orcid, email, department_school_lab,
                  institution, city, state_province, country, secondary_department_school_lab, secondary_institution,
                  secondary_city, secondary_state_province, secondary_country, section_title, section_seq_no,
                  published_article_number, start_page, end_page, article_seq_no, art_submission_date,
                  art_approval_date,
                  source, abstract, sep=',', file=output)
            author_sequence += 1


if __name__ == '__main__':
    authors = pandas.read_csv('authors.csv')
    accepted = pandas.read_csv('accepted.csv')
    with open('output_acm.csv', 'w') as output:
        process_submissions(accepted, authors, output)
