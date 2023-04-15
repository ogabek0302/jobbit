from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from selenium import webdriver
from selenium.webdriver.common.by import By

def job_list(request):
    if request.method == 'POST':
        jobs = scrape_jobs()
        for job in jobs:
            job.save()
    else:
        jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'job_list.html', context)

def scrape_jobs():
    url = 'https://www.indeed.com/jobs?q=python+developer&l=New+York%2C+NY'
    driver = webdriver.Chrome()
    driver.get(url)

    jobs = []
    job_elements = driver.find_elements(By.XPATH, "//div[@class='jobsearch-SerpJobCard']")
    for element in job_elements:
        title_element = element.find_element(By.XPATH, ".//h2[@class='title']/a")
        title = title_element.text
        company_element = element.find_element(By.XPATH, ".//span[@class='company']")
        company = company_element.text
        location_element = element.find_element(By.XPATH, ".//div[@class='recJobLoc']")
        location = location_element.get_attribute('data-rc-loc')
        description_element = element.find_element(By.XPATH, ".//div[@class='summary']")
        description = description_element.text
        salary_element = element.find_element(By.XPATH, ".//span[@class='salaryText']")
        salary = salary_element.text if salary_element else None

        job = Job(
            title=title,
            company=company,
            location=location,
            description=description,
            salary=salary
        )
        jobs.append(job)

    driver.quit()
    return jobs
    