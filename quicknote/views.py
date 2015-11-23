from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import NoteForm
from quicknote.models import Notebook
import shortuuid


def index(request):
	if request.method == 'POST':
		if 'userkey' in request.POST:
			#print("right")
			book = request.POST.get('userkey')
			if Notebook.objects.filter(bookname = book).exists():
				return HttpResponseRedirect(reverse('quicknote:notebook',args=(book,)))
			else:
				msg = "Notebook with the key you entered doesn't exist."
				return render(request,'quicknote/error.html',{'errormsg':msg})
		else:
			print("left")
			form = Notebook()
			key = shortuuid.uuid()
			form.bookname = key
			form.note = 'Your key is ' + key
			form.title = 'Quicknote'
			form.noteid = shortuuid.uuid()
			form.save()
			#print(form.bookname)
			return HttpResponseRedirect(reverse('quicknote:notebook',args=(form.bookname,)))
	return render(request,'quicknote/index.html',{})


def notebook(request,nid):
	if request.method== "POST":
		form = NoteForm(request.POST)
		print("Before valid")
		if form.is_valid():
			print("After valid")
			note = form.save(commit=False)
			note.bookname=nid
			note.noteid = shortuuid.uuid()
			note.save()
			return HttpResponseRedirect(reverse('quicknote:notebook',args=(note.bookname,)))
		else:
			form = NoteForm()
	if Notebook.objects.filter(bookname = nid).exists():
		note=Notebook.objects.filter(bookname=nid)
		return render(request,'quicknote/notebook.html',{'note':note})
	else:
		msg = "Notebook doesn't exist."
		return render(request,'quicknote/error.html',{'errormsg':msg})


def note(request,qnoteid):
	if Notebook.objects.filter(noteid = qnoteid).exists():
		note=Notebook.objects.filter(noteid=qnoteid)
		return render(request,'quicknote/note.html',{'note':note})
	else:
		msg = "Note doesn't exist."
		return render(request,'quicknote/error.html',{'errormsg':msg})


def redir(request):
	return HttpResponseRedirect(reverse('quick:redir'))