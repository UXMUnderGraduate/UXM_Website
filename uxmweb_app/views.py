from django.shortcuts import render

# Create your views here.
def publication(request):
    paper_table = [{
            "is_latest":True,
            "year_data":"2020",
            "journal_paper_list" : [{
                "title":"논문 제목1",
                "author":"논문 저자1",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목2", 
                "author":"논문 저자2",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }],
            "conference_paper_list" : [{
                "title":"논문 제목3",
                "author":"논문 저자3",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목4", 
                "author":"논문 저자4",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }]
        },{
            "is_latest":False,
            "year_data" : "2019",
            "journal_paper_list" : [{
                "title":"논문 제목1",
                "author":"논문 저자1",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목2", 
                "author":"논문 저자2",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }],
            "conference_paper_list" : [{
                "title":"논문 제목3",
                "author":"논문 저자3",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목4", 
                "author":"논문 저자4",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }]
        }
    ]
    return render(request, 'publication.html', {"paper_table":paper_table})

def project(request):
    pj = "pj"
    return render(request, 'project.html',{"pj":pj})
def notice(request):
    notice_list = [
        {"number":1,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O",
        "content":"test"},
        {"number":2,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O"},
        {"number":3,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O"},
        {"number":4,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O"},
        {"number":5,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O"},
        {"number":6,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"X"},
        {"number":7,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O"},
        {"number":8,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O"},
        {"number":9,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"X"},
        {"number":10,
        "title":"명지대학교 uxm 공지사항",
        "date":"20/10/06",
        "writer":"관리자",
        "view":1,
        "file":"O"},

    ]

    return render(request, 'notice.html',{"notice_list":notice_list})
def main(request):
    return render(request, 'main.html')
    
def member(request):
    return render(request, 'member.html')

def photo(request):
    paper_table = [{
            "is_latest":True,
            "year_data":"2020",
            "journal_paper_list" : [{
                "title":"논문 제목1",
                "author":"논문 저자1",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목2", 
                "author":"논문 저자2",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }],
            "conference_paper_list" : [{
                "title":"논문 제목3",
                "author":"논문 저자3",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목4", 
                "author":"논문 저자4",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }]
        },{
            "is_latest":False,
            "year_data" : "2019",
            "journal_paper_list" : [{
                "title":"논문 제목1",
                "author":"논문 저자1",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목2", 
                "author":"논문 저자2",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }],
            "conference_paper_list" : [{
                "title":"논문 제목3",
                "author":"논문 저자3",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"},
                {
                "title":"논문 제목4", 
                "author":"논문 저자4",
                "publication_data":"어디어디학술지 몇년 몇월 몇일"
                }]
        }
    ]
    return render(request, 'photo.html', {"paper_table":paper_table})